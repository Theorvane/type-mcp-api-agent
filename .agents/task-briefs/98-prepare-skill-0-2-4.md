# Task brief: 98 — prepare api-to-typemcp 0.2.4 security release

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/98
**Branch:** `chore/98-prepare-skill-0-2-4`
**Owner:** sjungwon03

## Goal

Prepare an immutable `api-to-typemcp` 0.2.4 release that publishes the verified generated-project dependency security fixes.

## Source references

- Release contract: `.agents/scripts/test_skill_release.py`
- Release workflow: `.github/workflows/skill-release.yml`
- Skill metadata: `skills/api-to-typemcp/SKILL.md`
- Repository release link: `README.md`
- Security remediations: Issues #94 and #95

## Scope

### Included

- Advance release metadata and release-contract fixtures from `0.2.3` to `0.2.4`.
- Preserve all runtime guidance, including `@theorvane/type-mcp@0.3.2`.
- Validate generated template production audit and protected promotion readiness.

### Excluded

- Creating tags, GitHub Releases, or external registry publications before promotion to `main`.
- Changing prior immutable `v0.2.3` release history.
- Further dependency changes beyond merged #94 and #95.

## Safety and contract notes

- `v0.2.4` does not currently exist in GitHub tags or Releases.
- `main` is an ancestor of the current `dev` base; no reconciliation was necessary at branch creation.
- The release workflow creates a GitHub Release and registry publications only from a verified `main` push after protected promotion.

## Test-first evidence

| Stage | Command | Expected/observed result |
| --- | --- | --- |
| Red | `python3.11 .agents/scripts/test_skill_release.py` | Observed expected failure: workflow emitted `skill_version=0.2.3` / `tag=v0.2.3` while the immutable release contract required `0.2.4` / `v0.2.4`. |
| Green | same command | Passed: 19 release-contract tests with `0.2.4` fixtures. |
| Regression | docs/workspace/E2E/template audit | Passed docs/workspace validation, contained generated-project E2E, Python compile, and rendered-template production audit (0 vulnerabilities). |

## Verification

- [x] Release contract
- [x] Documentation and workspace validation
- [x] Generated-project E2E
- [x] Rendered template production audit
- [x] `git diff --check`
- [x] Independent review

## Review notes

- `v0.2.4` was confirmed absent before release preparation; no immutable tag or published release was changed.
- `main` remained an ancestor of the starting `dev` SHA, so this is a normal dev-to-main protected promotion candidate.