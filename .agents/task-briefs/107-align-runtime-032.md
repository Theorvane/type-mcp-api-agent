# Task brief: 107 — align generated TypeMCP runtime dependency

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/107
**Branch:** `fix/107-align-runtime-032`
**Owner:** `sjungwon03`

## Problem
The public `api-to-typemcp@0.2.5` ClawHub scanner correctly identified that user-facing guidance says `@theorvane/type-mcp@0.3.2`, while the generated TypeScript stdio package template and deterministic package lock resolve `0.2.0`.

## Scope
- Align the generated template package dependency and package lock with the published `@theorvane/type-mcp@0.3.2` runtime.
- Add deterministic version, registry URL, and SRI integrity contracts for the direct generated runtime dependency.
- Update existing generated-project render/E2E runtime contracts to `0.3.2`.
- Verify generated project install, typecheck, tests, build, stdio MCP smoke, and production audit.

## Safety constraints
- Do not alter existing immutable `v0.2.5`/`0.2.5` artifacts or republish them.
- Preserve standard root/ESM and legacy subpath/CJS documentation separation.
- Preserve patched transitive resolutions: fast-uri `3.1.5`, postcss `8.5.24`, hono `4.12.34`.
- Generated package must only use npm registry provenance; no `file:`, `git:`, or `link:` runtime source.
- No agent installation gate changes are in scope.

## Test record
| Phase | Command | Result |
|---|---|---|
| Baseline | `python3.11 -m unittest discover -s skills/api-to-typemcp/tests -p 'test_generated_project_e2e.py' -v` | 6 tests passed while asserting obsolete `0.2.0`; confirms the test required correction. |
| Red | focused security/render/E2E suite | Observed expected 3 failures: template and generated package still resolved `0.2.0` while contracts required `0.3.2`. |
| Green | same focused suite | 30 tests passed after template, deterministic lock, and runtime contracts were aligned. |
| Regression | release/docs/workspace suites, Python compile, `git diff --check` | Passed: release 19 tests; docs 8; workspace 3; compile and diff checks clean. |
| Consumer | rendered template `npm ci --ignore-scripts` + `npm audit --omit=dev --json` | Installed 142 packages; exact runtime `0.3.2` URL/SRI and patched fast-uri/postcss/hono resolutions verified; audit reports 0 vulnerabilities. |
| Independent review | Codex read-only review | Initial medium finding (E2E checked only rendered declaration) was resolved. Final review found no blocking issues; E2E now asserts the version from isolated installed `node_modules` plus lockfile registry URL/SRI. |

## External evidence
- npm metadata for `@theorvane/type-mcp@0.3.2`: tarball `https://registry.npmjs.org/@theorvane/type-mcp/-/type-mcp-0.3.2.tgz`, SRI `sha512-Rpspxnyl+UZeeakhng9PSCdsnVM4BTBkZ2XQsI5/ywoAU8OAKUMS+DQntY6aNCCgTtzwb3u0Wq7YVrSxfRwwWg==`.
- Published ClawHub `0.2.5` scanner called out the exact docs/template version mismatch.
