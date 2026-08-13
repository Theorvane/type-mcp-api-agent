# Task brief: 109 — prepare api-to-typemcp 0.2.6

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/109
**Branch:** `chore/109-prepare-skill-0-2-6`

## Scope
Prepare the immutable `api-to-typemcp@0.2.6` patch release containing the verified generated-runtime alignment from #107/#108.

- Update SKILL metadata, README GitHub Release link, and release-contract fixtures to `0.2.6` / `v0.2.6`.
- Keep documented/generated `@theorvane/type-mcp@0.3.2` runtime unchanged.
- Do not mutate existing `v0.2.5` artifacts.

## Evidence
- Baseline: release contract passed 19 tests at `0.2.5`.
- `v0.2.6` GitHub tag and Release are both absent before changes.
- #108 merge CI passed at `9d7457fda68d3875a29b0fdbe3429e270f147411`.

## Validation
| Phase | Result |
|---|---|
| Red | `python3.11 .agents/scripts/test_skill_release.py` | Expected 5 failures/errors: fixture required `0.2.6` while canonical SKILL metadata remained `0.2.5`. |
| Green | release contract and full suites | Passed: release 19; runtime docs 2; docs 8; workspace 3; generated security/render/static/E2E 30. |
| Regression | compile/diff and rendered consumer | Python compile and diff check clean; consumer installed exact `0.3.2` runtime and production audit reported 0 vulnerabilities. |
