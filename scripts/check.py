#!/usr/bin/env python3
"""Checks the skills: size budgets, frontmatter, paths and skill names, versions and the discovery index."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

# Descriptions are listed on every turn; an entry is read in full when its skill opens.
DESCRIPTION_MAX = 320
ENTRY_MAX = {"invideo": 7168}
ENTRY_DEFAULT_MAX = 5120
# Every SKILL.md stays short and routes to its references.
ENTRY_LINES_MAX = 120

MANIFESTS = [".claude-plugin/plugin.json", ".codex-plugin/plugin.json", ".cursor-plugin/plugin.json"]

PATH_RE = re.compile(r"`(references/[\w./-]+\.md)`|\]\(((?!https?:)[\w./-]+\.md)\)")
SKILL_RE = re.compile(r"`/(invideo[\w-]*|[\w-]+-to-invideo)`")


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        fields[key.strip()] = json.loads(value) if value.startswith('"') else value
    return fields


def check_skills():
    problems = []
    names = {d.name for d in SKILLS.iterdir() if d.is_dir()}
    for skill in sorted(names):
        entry = SKILLS / skill / "SKILL.md"
        if not entry.is_file():
            problems.append(f"{skill}: no SKILL.md")
            continue
        text = entry.read_text()
        fields = frontmatter(text)
        if fields is None:
            problems.append(f"{skill}: no frontmatter")
            continue
        if fields.get("name") != skill:
            problems.append(f"{skill}: name is {fields.get('name')!r}, not the folder name")
        description = fields.get("description", "")
        if not description:
            problems.append(f"{skill}: no description")
        elif len(description.encode()) > DESCRIPTION_MAX:
            problems.append(f"{skill}: description is {len(description.encode())} B, over {DESCRIPTION_MAX} B")
        budget = ENTRY_MAX.get(skill, ENTRY_DEFAULT_MAX)
        if len(text.encode()) > budget:
            problems.append(f"{skill}/SKILL.md is {len(text.encode())} B, over its {budget} B budget")
        lines = len(text.splitlines())
        if lines >= ENTRY_LINES_MAX:
            problems.append(f"{skill}/SKILL.md is {lines} lines; keep it under {ENTRY_LINES_MAX}")

        for md in sorted((SKILLS / skill).rglob("*.md")):
            body = md.read_text()
            rel = md.relative_to(SKILLS)
            for code_path, link_path in PATH_RE.findall(body):
                # Backticked paths are relative to the skill folder, links to the file.
                target = (SKILLS / skill / code_path) if code_path else (md.parent / link_path)
                if not target.is_file():
                    problems.append(f"{rel}: {code_path or link_path} does not exist")
            for name in SKILL_RE.findall(body):
                if name not in names:
                    problems.append(f"{rel}: skill /{name} does not exist")
    return problems


def check_manifests():
    problems, versions = [], {}
    for path in MANIFESTS:
        try:
            versions[path] = json.loads((ROOT / path).read_text()).get("version")
        except (OSError, ValueError) as e:
            problems.append(f"{path}: {e}")
    try:
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        versions[".claude-plugin/marketplace.json"] = marketplace["plugins"][0].get("version")
    except (OSError, ValueError, KeyError, IndexError) as e:
        problems.append(f".claude-plugin/marketplace.json: {e}")
    try:
        versions["VERSION"] = (ROOT / "VERSION").read_text().strip()
    except OSError as e:
        problems.append(f"VERSION: {e}")
    if len(set(versions.values())) > 1:
        problems.append("versions differ: " + ", ".join(f"{p} {v}" for p, v in versions.items()))
    return problems

def check_index():
    """index.json, served at /.well-known/skills/index.json, lists every skill folder with its files."""
    try:
        index = json.loads((ROOT / "index.json").read_text())
    except (OSError, ValueError) as e:
        return [f"index.json: {e}"]
    problems = []
    entries = {e.get("name"): e for e in index.get("skills", [])}
    folders = {d.name for d in SKILLS.iterdir() if d.is_dir()}
    for name in sorted(folders - entries.keys()):
        problems.append(f"index.json: {name} is missing")
    for name in sorted(entries.keys() - folders):
        problems.append(f"index.json: {name} is not a skill folder")
    for name in sorted(folders & entries.keys()):
        entry = entries[name]
        fields = frontmatter((SKILLS / name / "SKILL.md").read_text()) or {}
        if entry.get("description") != fields.get("description"):
            problems.append(f"index.json: {name} description differs from its SKILL.md")
        files = sorted(str(p.relative_to(SKILLS / name)) for p in (SKILLS / name).rglob("*") if p.is_file())
        if sorted(entry.get("files", [])) != files:
            problems.append(f"index.json: {name} files differ from the folder")
    return problems


def main():
    problems = check_skills() + check_manifests() + check_index()
    for p in problems:
        print(f"✗ {p}")
    if problems:
        sys.exit(1)
    print("✓ skills within budget; paths, skill names, versions and index resolve")


if __name__ == "__main__":
    main()
