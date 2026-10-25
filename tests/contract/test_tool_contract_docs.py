"""Every registered tool has its own contract row (issue #793).

`docs/tool-contracts.md` is the source of truth for the tool surface. The audit
in #793 found three tools without a row of their own (one combined row counted a
single row for two tools, and one tool was described only in prose), so this
pins registry membership to the document and keeps it from drifting again.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from fastmcp import FastMCP
from fastmcp.server.providers.base import Provider

from mcp_server.bridge import Bridge
from mcp_server.config import ServerConfig
from mcp_server.server import create_server, register_tool_transform
from tests.fakes import FakeAddonConnection, connector_for, make_addon_responder

pytestmark = pytest.mark.asyncio

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTRACTS = REPO_ROOT / "docs" / "tool-contracts.md"

# A row that documents exactly one tool: `| `godot_x` | params | returns | class |`.
# Combined rows such as "`godot_a` / `godot_b`" deliberately do not match: #793
# requires a row per tool so the row count can be compared with the registry.
ROW = re.compile(r"^\s*\|\s*`(?P<tool>godot_[a-z0-9_]+)`\s*\|.*\|\s*$")


def _rows() -> dict[str, list[int]]:
    """Tool name -> the line numbers of the rows that document it."""
    rows: dict[str, list[int]] = {}
    for number, line in enumerate(CONTRACTS.read_text(encoding="utf-8").splitlines(), 1):
        match = ROW.match(line)
        if match is not None:
            rows.setdefault(match.group("tool"), []).append(number)
    return rows


def _server() -> FastMCP:
    config = ServerConfig()
    conn = FakeAddonConnection(make_addon_responder())
    bridge = Bridge(config.bridge, connector=connector_for(conn))
    return create_server(config, bridge=bridge)


async def test_every_registered_tool_has_a_row_of_its_own() -> None:
    server = _server()
    await register_tool_transform(server)
    tools = await Provider.list_tools(server)
    assert tools, "no tools registered"

    rows = _rows()
    missing = sorted(tool.name for tool in tools if tool.name not in rows)
    assert not missing, f"docs/tool-contracts.md has no single-tool row for: {', '.join(missing)}"


async def test_no_tool_is_documented_twice() -> None:
    duplicated = {tool: lines for tool, lines in _rows().items() if len(lines) > 1}
    assert not duplicated, f"docs/tool-contracts.md documents a tool more than once: {duplicated}"
