# Task brief: 103 — prepare api-to-typemcp 0.2.5

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/103
**Branch:** `chore/103-prepare-skill-0-2-5`
**Owner:** sjungwon03

## Goal

Prepare the immutable `api-to-typemcp` `0.2.5` release so the reviewed ClawHub propagation hardening on `dev` can be promoted without changing the existing `v0.2.4` tag or release.

## Scope

### Included

- Advance the canonical skill version, README GitHub Release link, and version-specific release-contract fixtures from `0.2.4` to `0.2.5`.
- Preserve the current TypeMCP runtime guidance (`@theorvane/type-mcp@0.3.2`) and release workflow safety behavior.

### Excluded

- Direct updates to `main`, tag creation, GitHub Release creation, or registry publication.
- Dependency changes or generated-template modifications.
- Any mutation to immutable `v0.2.4` artifacts.

## Safety and contract notes

- Side effects: this preparation PR only changes the future release identity. The protected promotion and workflow own publication.
- Compatibility: runtime package guidance remains pinned to `@theorvane/type-mcp@0.3.2`.
- Version safety: `v0.2.5` was confirmed absent from GitHub Releases before preparation.

## Test-first evidence

| Stage | Command | Expected/observed result |
| --- | --- | --- |
| Red | `python3.11 .agents/scripts/test_skill_release.py` | Observed expected failure: extracted `skill_version=0.2.4` / `tag=v0.2.4` did not satisfy the new `0.2.5` contract. |
| Green | same command | Passed: 19 release-contract tests with `0.2.5` fixtures. |
| Regression | release/docs/workspace/generated-project validation | Passed runtime docs (2), docs harness (8), workspace (3), generated-project E2E (6), Python compile, diff check, and rendered template production audit (0 vulnerabilities). |

## Verification

- [x] Release contract
- [x] Documentation and workspace validation
- [x] Generated-project E2E
- [x] `git diff --check`
- [x] Independent review

## Review notes

- `main` is an ancestor of `dev`; no history reconciliation is needed before release preparation.
- The change leaves `@theorvane/type-mcp@0.3.2`, lockfiles, templates, and ClawHub failure semantics unchanged.