# Task brief: 92 — reconcile pending ClawHub publication

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/92
**Branch:** `fix/92-reconcile-clawhub-pending`
**Owner:** sjungwon03

## Goal

Make the skill release workflow verify ClawHub's asynchronous public publication without creating a duplicate immutable version.

## Source references

- Release workflow: `.github/workflows/skill-release.yml`
- Release guide: `docs/guides/skill-release.md`
- Pinned ClawHub CLI: `openclaw/clawhub@306035cad779533e212a1fafd4c9938ea4c0b70e`

## Scope

### Included

- Poll the official public immutable version endpoint after the single publish submission.
- Accept documented `pending-publication`/`pending` only while polling the exact version.
- Fail closed on timeout, unexpected HTTP response, malformed payload, or version mismatch.
- Add offline contracts for pending-to-published and failure paths.

### Excluded

- Retagging or changing GitHub Release `v0.2.3`.
- Republishing the existing ClawHub `0.2.3` submission.
- Changing skill content or its version.

## Safety and contract notes

- Side effects: exactly one existing `skill publish` command remains; verification only issues public GET requests.
- Credentials: the helper takes no credentials and never logs tokens.
- Compatibility: the endpoint is the pinned official CLI's inspect endpoint.

## Test-first evidence

| Stage | Command | Expected/observed result |
| --- | --- | --- |
| Red | `python3.11 .agents/scripts/test_skill_release.py` | Failed because the workflow had no pending-publication reconciliation path. |
| Green | `python3.11 .agents/scripts/test_skill_release.py` | Passed: 19 tests covering pending-to-published, timeout, non-404 failure, malformed JSON, version mismatch, and one publish mutation. |
| Regression | repository verification baseline plus contained E2E | Passed: runtime docs, docs harness, workspace validation, documentation validation, contained E2E, Python compile, and `git diff --check`. |

## Verification

- [ ] Release contract tests
- [ ] Documentation validation
- [ ] Contained generated-project E2E
- [ ] Python compile
- [ ] `git diff --check`
- [ ] Independent review

## Review notes

- The original `0.2.3` release submitted successfully to ClawHub and returned pending while scans completed. The public endpoint later exposed the exact immutable version.