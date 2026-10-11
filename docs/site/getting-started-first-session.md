---
type: index
title: "Your first session"
description: "Install the skill, then drive a real Godot project from your AI assistant — the orient → enable → preview → act → verify rhythm."
created: 2026-09-19
updated: 2026-10-11
---

# Your first session

godot-mcp is driven **through an AI assistant**, not by typing tool names. So the
single most useful thing you can do first is **install the skill** — a small bundle
of knowledge your assistant loads automatically. It teaches it to:

- check the bridge and version before it starts,
- **enable the toolset it needs, by itself** (you never manage gates), and
- read the "what actually happened" fields and avoid the Godot pitfalls that trip agents up.

→ **[Install the skills](reference-skills.md)** (`./scripts/install-skills.sh`), then
restart your assistant. From then on it just knows how to work in Godot.

With the skill in place you talk in plain language and supervise in Godot. The rhythm is
always the same: **orient → enable → preview → act → verify.**

::: info Under the hood
Each stage below shows **what you ask**, then — **under the hood** — the `godot_*` calls
your assistant makes. **You never type them**; they're shown so you can follow along and
spot a stall.
:::

::: warning No skill installed?
The workflow degrades gracefully without it, but the assistant won't know to enable
toolsets on its own or to read the honesty fields — you'll be prompting it about
`unknown tool` errors and stale-save verdicts yourself. Install the skill.
:::

## 1. Orient — ask the agent to check the bridge

You: *"Check that Godot is connected and tell me what's available."*

```
godot_health_check()        # bridge connected? which version?
godot_get_server_info()     # capability snapshot: toolsets, active scene, next_steps
godot_list_toolsets()       # what exists, what's enabled, min Godot per toolset
```

If the agent reports `bridge_connected: false`, the editor isn't reachable —
open Godot with the [addon enabled](getting-started-addon.md), check the status
dock (bottom panel), and ask again. `godot_get_server_info` is the single most
useful call: its `next_steps` field usually names the fix for whatever is wrong.

## 2. Enable what you need — the assistant handles it

Ask for something that needs a gated toolset and the assistant turns it on for you —
this is the part the getting-started skill teaches, so you don't have to think about it.

You: *"Add a Player node to the main scene."*

```
godot_enable_toolset('scene_edit')    # the assistant enables what the task needs
godot_enable_toolset('scripts')
```

If your assistant instead stalls on `unknown tool`, it's missing the skill (or hasn't
enabled the toolset) — prompt it: *"enable the toolset you need first"*, or
[install the skill](reference-skills.md). `godot_list_toolsets()` is always
authoritative.

## 3. Inspect before mutating — the agent reads, then edits

You: *"What's in the scene right now?"*

```
godot_inspection_get_scene_tree()          # the tree; paths are tool-ready
godot_inspection_get_selected_node()       # what you have selected in the editor
godot_inspection_get_project_info()        # autoloads, input actions, main scene
```

Node paths come back scene-relative (`"."`, `"Player/Weapon"`) in exactly the
form the path-taking tools accept — the agent passes them verbatim. You can see
the same thing live in Godot's Scene dock.

## 4. Preview, then act — you approve, the agent mutates

You: *"Create the Player node — preview it first."*

```
godot_scene_edit_create_node(parent_path=".", node_type="CharacterBody2D",
                             node_name="Player", dry_run=true)
# preview: {node_path: "Player", created: false, persisted: <verdict>}
godot_scene_edit_create_node(parent_path=".", node_type="CharacterBody2D", node_name="Player")
# real:   {node_path: "Player", created: true, persisted: true}
```

`dry_run` runs the same preconditions and persistence probe the real run will —
worth asking for on unfamiliar scenes. When the agent acts, the change lands in
**your** editor: watch it appear in the Scene dock, and press **Ctrl+Z** to
undo it. Every mutation is on the editor undo stack, so the agent's actions are
as revertible as your own.

## 5. Verify — ask the agent to prove it worked

You: *"Check the script parses and the scene runs without errors."*

```
godot_scripts_get_parse_errors(script_path='res://scripts/player.gd')
godot_runtime_run_and_capture(scene='res://scenes/main.tscn', timeout_seconds=5)
```

A clean parse is *not* full verification — runtime API misuse needs the headless
run. Shaders need `godot_shader_validate`. The one-call diagnostics recipe is
`godot_debug_workflow()` (always-on `core`). Ask for the verdict, not just the
action.

## Reading the results the agent reports back

The agent's results carry **honesty fields** that read as ground truth — check
them (or ask the agent to explain them):

- `persisted: true` → the save will keep the change.
- `persisted: false, reason: instanced_child_not_editable` → the edit shows in
  the editor but **won't be saved**; act on the hint
  (`godot_scene_edit_set_editable_children(node_path='Relic')`), or retarget.
- `rescan_pending: true` on a parse check → the editor's file scan hadn't
  flushed; re-check once before "fixing" correct code.
- `aborted_at` on a batch → trailing commands did **not** run.

A well-behaved agent reads these and acts; you should ask it to when it doesn't.

## When something fails

| Error | Meaning | What to tell the agent |
|-------|---------|------------------------|
| `unknown tool` | toolset not enabled (or a server-side tool confused with an editor tool) | "enable the toolset first" |
| `PRECONDITION_FAILED [required=active_scene]` | no scene open | "open or create a scene" |
| `PRECONDITION_FAILED [required=confirm]` | destructive call needs confirmation | review it, then "confirm and retry" |
| `BRIDGE_DISCONNECTED` | editor not reachable | open Godot + addon; check the status dock |
| `VALIDATION_ERROR` with a did-you-mean | typo'd key/path | "use the suggested key" |

`godot_get_server_info()`'s `next_steps` and the `troubleshoot` prompt cover the
rest.

## Making it smoother

- **Reach for prompts.** The server's [workflow prompts](reference-prompts.md)
  (`/mcp__godot-mcp__build_scene`, `/play_test`, …) are step-numbered recipes the
  assistant can follow for a whole task — a skill points it at the right one.
- **Start from an example.** The two games under
  [examples](guides-examples.md) give the assistant a real project to work against.

Next: [Build a scene](guides-build-scene.md) walks the full loop, or
[Play-test & debug](guides-playtest-debug.md) starts from the runtime side.
