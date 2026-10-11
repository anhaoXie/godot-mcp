---
type: index
title: "Getting started"
description: "Install, connect, and drive your first Godot session through MCP."
created: 2026-09-19
updated: 2026-10-10
---

# Getting started

!!! tip "Just want to make a game?"
    If you use an AI assistant and would rather not deal with installs or MCP, start with
    **[Set up with your AI agent](getting-started-with-an-agent.md)** — the assistant does
    the setup. The four steps below are the manual / technical path.

Four steps, then you're driving the editor from an agent:

1. [Install the MCP server](getting-started-install.md) — PyPI, Docker, or from source.
2. [Install the Godot addon](getting-started-addon.md) — from the Godot Asset Library (**Godot Editor MCP - Addon**), or copy it into your project; then enable it.
3. [Configure your MCP client](getting-started-clients.md) — OpenCode, Claude, or any MCP host.
4. [Run your first session](getting-started-first-session.md) — inspect, then mutate, then verify.

Remote / multi-machine setups (OpenWebUI, Docker, HTTP transport) are covered
in [remote access](getting-started-openwebui.md).

## Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Godot** | 4.4 | 4.7 (validated target) |
| **Python** | 3.11 | 3.13 |
| **Package manager** | [uv](https://docs.astral.sh/uv/) | uv |
| **OS** | macOS / Linux / Windows | Any desktop |

!!! note "Godot 4.4 is the floor"
    The addon checks the editor version on enable and warns if it is older.
    Some toolsets (`scene_edit`, `input_map`, `tilemap`, `scene_3d`) are
    version-gated and refuse to enable on older editors.