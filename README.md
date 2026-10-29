<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/invideo-symbol-white.svg">
    <img alt="" src="assets/invideo-symbol-black.svg" height="40" align="absmiddle">
  </picture>
  &nbsp;invideo skills
</h1>

Skills that teach agents to create and edit videos with [invideo](https://invideo.io), a professional AI-native video editor. Your agent edits a real timeline; you watch every change land in the browser and can take over at any frame.

The skills hold what an agent cannot work out on its own: how invideo works, what each kind of video needs, and how to check the result. Exact commands come from invideo itself: `invideo --help`, or `get_help` over MCP.

## Install

Claude Code:

```sh
claude plugin marketplace add invideoio/skills
claude plugin install invideo@invideo
```

Codex:

```sh
codex plugin marketplace add invideoio/skills
codex plugin add invideo@invideo
```

Any agent, skills only:

```sh
npx skills add invideoio/skills
```

On first use the agent installs the [invideo CLI](https://github.com/invideoio/cli) and opens a browser tab for you to sign in. Agents without a shell, like claude.ai, use the hosted MCP server at `https://mcp.invideo.io/mcp` as a connector.

## Skills

| Skill | For |
|---|---|
| `invideo` | Read first: how to connect, the work loop, cost, and every job type, from launch videos and ads to invitations and captions |
| `invideo-media` | Uploads, stock, checking media, voice and music craft |
| `invideo-generate` | Images, video, voice, music, sound and 3D from AI models |
| `invideo-timeline` | Frame math, tracks, keyframes, color, effects and the mix |
| `invideo-pipeline` | Many videos from data, scripted runs, CI, several agents in one project |
| `higgsfield-to-invideo` | Finish Higgsfield clips: cuts, captions, music |
| `runway-to-invideo` | Finish Runway clips: cuts, captions, music |
| `magnific-to-invideo` | Finish Magnific video: layout, captions, music |
| `remotion-to-invideo` | Finish a Remotion composition: cuts, captions, music |
| `hyperframes-to-invideo` | Finish a HyperFrames composition: cuts, captions, music |
| `openedit-to-invideo` | Finish an OpenEdit plan: cuts, captions, music |

## Layout

- `skills/<name>/SKILL.md`, with depth in `references/` that loads only when a job needs it
- `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`: one manifest per agent, same version as `VERSION`
- `index.json`: the skills index
- `scripts/check.py`: size budgets, paths, skill names, versions and the index

## License

[Apache-2.0](LICENSE)
