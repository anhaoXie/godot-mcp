---
layout: home

hero:
  name: 'godot-mcp'
  text: 'Build your Godot game by talking to your AI'
  tagline: 'Your AI assistant drives a live Godot editor — inspecting, editing, running, and double-checking its own work, with every change undoable. No more editing files blind.'
  actions:
    - theme: brand
      text: Get started
      link: ./getting-started
    - theme: alt
      text: How it works
      link: ./concepts
    - theme: alt
      text: GitHub
      link: https://github.com/hybridindie/godot-mcp

features:
  - title: It works in your real editor
    details: Every action happens against the editor you have open — the scene you can see. Agent edits land on Godot's own undo stack, so Ctrl+Z works exactly like it does for you.
  - title: It tells the truth
    details: Results never fake success. Every edit says whether the save will really keep it, batches report what actually ran, and a timeout is never dressed up as a crash.
  - title: A small, sharp surface
    details: Only a handful of tools are on by default; the agent pulls in more only when a task needs them. A focused surface means better choices and fewer wasted calls.
  - title: Safe by construction
    details: Destructive actions ask first, previews are free, and every safety and permission decision lives on the server — never in the editor.
---

## See it catch a mistake

Ask your assistant to add a node inside an instanced scene:

```text
> add a marker node under Relic/Cold

{ "node_path": "Relic/Cold/Marker", "created": true,
  "persisted": false,
  "reason": "instanced_child_not_editable",
  "hint": "'Relic/Cold' is inside the instanced scene 'Relic', which doesn't have
           Editable Children enabled — the change shows in the editor but won't be
           saved. Enable Editable Children on 'Relic', or target a node the scene owns." }
```

A file-blind agent would just say *"done."* godot-mcp tells you **what will actually be saved** — and exactly how to fix it. That honesty is the whole point.

## Start in about two minutes

1. **Add the addon** to your Godot project and switch it on — *Project → Project Settings → Plugins → Godot Editor MCP - Addon*.
2. **Point your AI assistant at it** with one line in its MCP config (for Claude Code: `claude mcp add godot -- uvx godot-editor-mcp`).
3. **Tell it what you want** — *"add a player that jumps"*, *"make the jump feel snappier"*, *"why does it crash on start?"*.

New to all this? **[Start with your AI agent](./getting-started-with-an-agent)** walks it through step by step — your assistant does the installing. Prefer to do it yourself? **[Manual setup](./getting-started-install)**.

## Two ways in

- **Here to make a game?** Hand the setup to your assistant and build by describing what you want.
  → **[Start with your AI agent](./getting-started-with-an-agent)**
- **Here for the tool itself?** (you know MCP — and maybe want to contribute.)
  → **[Concepts](./concepts)** · **[Under the hood](./architecture/)** · **[Reference](./reference)** · **[Contributing](https://github.com/hybridindie/godot-mcp/blob/main/CONTRIBUTING.md)**

## Where to go next

- **[Get started](./getting-started)** — install, connect, and drive your first session
- **[Guides](./guides)** — build a scene, play-test & debug, verify your work, ship
- **[Concepts](./concepts)** — how it works, and why it's built this way
- **[Reference](./reference)** — every tool, safety class, error code, and setting
- **[Under the hood](./architecture/)** — the bridge, the envelope, gating, and safety

---

> **For AI agents.** This site ships [`llms.txt`](https://hybridindie.github.io/godot-mcp/llms.txt) (a page index) and [`llms-full.txt`](https://hybridindie.github.io/godot-mcp/llms-full.txt) (the whole site in one fetch).
