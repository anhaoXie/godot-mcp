---
type: index
title: "Get started"
description: "Install godot-mcp, connect your editor and AI assistant, and drive your first session."
created: 2026-09-19
updated: 2026-10-11
---

# Get started

Two ways to get running. Pick whichever fits.

## Option 1 — Let your AI assistant do it (easiest)

You use an AI assistant (Claude, Codex, ChatGPT…) and would rather not touch a terminal. Hand it the setup:

→ **[Start with your AI agent](getting-started-with-an-agent.md)** — one copy-paste prompt installs the server and the addon; you do one click and start building.

## Option 2 — Set it up yourself

You're comfortable with installs and MCP. Four steps:

1. **[Install the MCP server](getting-started-install.md)** — PyPI, Docker, or from source.
2. **[Install the Godot addon](getting-started-addon.md)** — from the [Godot Asset Store](https://store.godotengine.org/asset/john-d-studios/godot-editor-mcp-addon/) (**Godot Editor MCP - Addon**), or copy it in; then enable it.
3. **[Configure your client](getting-started-clients.md)** — OpenCode, Claude, or any MCP host.
4. **[Run your first session](getting-started-first-session.md)** — the orient → enable → preview → act → verify rhythm.

Running several clients against one editor, or driving Godot remotely? See
**[Remote & multi-client](getting-started-openwebui.md)**.

## Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Godot** | 4.4 | 4.7 (validated target) |
| **Python** | 3.11 | 3.13 |
| **Package manager** | [uv](https://docs.astral.sh/uv/) | uv |
| **OS** | macOS / Linux / Windows | Any desktop |

::: info Godot 4.4 is the floor
The addon checks the editor version on enable and warns if it's older. A few toolsets
(`scene_edit`, `input_map`, `tilemap`, `scene_3d`) are version-gated and refuse to
enable on older editors.
:::

New to the ideas behind any of this? **[Concepts](concepts.md)** explains the mental
model in five short ideas.
