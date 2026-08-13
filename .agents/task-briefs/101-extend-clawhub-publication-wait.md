# Task brief: 101 — allow bounded ClawHub publication propagation

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/101
**Branch:** `fix/101-extend-clawhub-publication-wait`

## Goal

Allow the one already-submitted ClawHub skill version enough bounded time to become publicly verifiable, without permitting duplicate publication.

## Scope

### Included

- Increase the workflow's public GET-only polling budget from 12 × 10 seconds to 36 × 10 seconds.
- Update release-contract coverage for that exact bounded configuration.

### Excluded

- Any additional `skill publish`, GitHub Release, tag, or registry mutation.
- Changing timeout, malformed-response, version-mismatch, or non-404 fail-closed behavior.
- Altering the already public immutable `0.2.4` artifact.

## Test-first evidence

| Stage | Command | Expected/observed result |
| --- | --- | --- |
| Red | `python3.11 .agents/scripts/test_skill_release.py` | Observed expected failure: workflow still contained `--attempts 12` while contract required `--attempts 36`. |
| Green | same command | Passed: 19 release-contract tests; workflow permits up to 36 GET-only public checks. |
| Regression | docs/workspace/E2E and release validation | Passed docs/workspace validation, contained E2E, Python compile, diff check, and an explicit one-check timeout fail-closed test. |

## Verification

- [x] Release contract
- [x] Documentation/workspace validation
- [x] Generated-project E2E
- [x] `git diff --check`
- [x] Independent review

## Review notes

- Main release workflow `31658205264` submitted exactly once at `2026-08-13T01:38:26Z` and received documented `pending-publication` for `api-to-typemcp@0.2.4` (`fileCount: 50`). Its original 12 × 10-second public GET waiter timed out at `2026-08-13T01:40:45Z`; no retry submission was made.
- At `2026-08-13T01:42Z` (after the failed waiter), a local GET-only command successfully returned `Verified public ClawHub version api-to-typemcp@0.2.4.` from `https://clawhub.ai/api/v1/skills/api-to-typemcp/versions/0.2.4` using 36 attempts and the same 10-second delay. The public payload reported version `0.2.4`, 50 files, and clean security status.
- GitHub immutable `v0.2.4` targets main merge `0178772a62d8f8ccfcc59763de633655a150e4b3`; skills-hub.ai reports `latestVersion: 0.2.4`.
- The workflow still has exactly one `skill publish skills/api-to-typemcp` invocation.
- The waiter stays GET-only after submission and remains fail-closed on timeout, malformed JSON, mismatched versions, and non-404 failures.
