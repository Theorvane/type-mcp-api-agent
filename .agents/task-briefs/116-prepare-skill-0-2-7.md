# Task brief: 116 — prepare api-to-typemcp 0.2.7

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/116
**Branch:** `chore/116-prepare-skill-0-2-7`

## Scope
Prepare the immutable `api-to-typemcp@0.2.7` patch release containing the reviewed TypeMCP 0.4.0 and MCP SDK v2 generated-project upgrade from #114/#115.

- Update SKILL metadata, README GitHub Release link, and release-contract fixtures to `0.2.7` / `v0.2.7`.
- Keep the reviewed generated `@theorvane/type-mcp@0.4.0` and split MCP client v2 contracts unchanged.
- Do not mutate existing `v0.2.6` artifacts.

## Evidence
- Baseline release contract passed at `0.2.6`.
- `v0.2.7` GitHub tag and Release are absent before changes.
- #115 merge CI passed at `2548c2b131e092742385cde4e554813a70f4fed2`.

## Validation
| Phase | Result |
|---|---|
| Red | `python3 .agents/scripts/test_skill_release.py` | 5 expected failures/errors while canonical metadata remained 0.2.6. |
| Green | release contract and full suites | Release contract: 19 passed. Full discovery: 143 passed. |
| Regression | compile/diff and generated consumer E2E | Documentation validation, workspace tests, Python compilation, generated-project E2E, and diff checks passed. |
