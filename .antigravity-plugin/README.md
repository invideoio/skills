# invideo for Antigravity

[invideo](https://invideo.io) is a professional AI-native video editor. This plugin connects your Antigravity agent to it. The agent opens your projects, generates video, voice and music, and trims, grades and mixes on a real multitrack timeline that you watch in the browser and can take over at any frame. Describe the edit in plain words, review the cut, export.

Works in the Antigravity app and the `agy` CLI.

## Before you start

- An invideo account. Sign up at [invideo.io](https://invideo.io).
- A terminal the agent can use. The plugin works through the [invideo CLI](https://github.com/invideoio/cli), not an MCP server.

## First use

On your first video request the agent:

1. Installs the invideo CLI if it is missing. It is a single binary in `~/.local/bin`, with no sudo. The agent tells you before it installs.
2. Runs `invideo auth login`, which opens a sign-in tab in your browser. Sign in, choose the workspaces the agent may use, and come back to Antigravity.

No browser (SSH, a container, a cloud machine): the agent signs in with `INVIDEO_NO_BROWSER=1` and sends you a link and code to approve on another device. The agent never asks for your password.

## What it costs

Generating media spends invideo credits. The agent dry-runs any call that costs 1 credit or more and waits for your approval before spending. Cheaper calls run on their own, and the agent tells you the cost afterwards.

## Try it

- "List my invideo projects"
- "Make a project from the clips in this folder, cut a 30-second vertical ad, caption it and add music"
- "Grade this video to golden hour and duck the music under the voice-over"
- "Turn this CSV of products into one short video per row"
- "I have clips from Runway: put them in order, add captions and music, export"

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

## Help

- Setup and fixes: [docs.invideo.io/start/antigravity](https://docs.invideo.io/start/antigravity)
- All docs: [docs.invideo.io](https://docs.invideo.io)
- Support: [help.invideo.io](https://help.invideo.io/) or support@invideo.io
- [Privacy policy](https://invideo.io/privacy-policy/) · [Terms of service](https://invideo.io/terms-of-service/)
