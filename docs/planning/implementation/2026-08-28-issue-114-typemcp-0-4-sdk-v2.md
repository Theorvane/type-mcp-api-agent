# Task brief: 114 — Generate TypeMCP 0.4.0 SDK v2 stdio projects

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/114
**Branch:** `feat/114-typemcp-0-4-sdk-v2`
**Owner:** Codex

## Goal

Generated stdio projects use the published TypeMCP 0.4.0 and split MCP client v2 contracts, including factory-based 2025/2026 stdio negotiation.

## Source references

- Product: `docs/product/mvp-scope.md`
- Architecture/API: `docs/architecture/overview.md`, `docs/api/manifest-contract.md`
- Runtime contract: `skills/api-to-typemcp/references/type-mcp-runtime.md`

## Scope

### Included

- TypeMCP 0.4.0 exact dependency and reviewed lockfile
- `serveStdioServer` generated startup
- split `@modelcontextprotocol/client` 2.0.0 smoke verification
- bundled docs, tests, and contained E2E updates

### Excluded

- HTTP, OAuth, resources, prompts, Tasks, media, visibility, skill release, or generated repository publication

## Safety and contract notes

- Source input: unchanged bounded supplied-document validation
- Secrets: values remain excluded from artifacts and smoke environments stay minimal
- Side effects: contained local generation/verification only; no publication
- Compatibility: generated projects intentionally move from 2025-only SDK v1 startup to TypeMCP 0.4.0 dual-era stdio serving

## Test-first evidence

| Stage | Command | Expected/observed result |
| --- | --- | --- |
| Red | `python3 skills/api-to-typemcp/tests/test_runtime_documentation.py` and `python3 skills/api-to-typemcp/tests/test_verify_generated_security.py` | Expected failure on old 0.3.2, SDK v1, and startStdioServer contracts |
| Green | same focused command | 2 runtime-documentation tests and 4 dependency/security tests passed |
| Regression | repository baseline plus generated-project E2E | required harness passed; 6 generated-project install/build/stdio E2E tests passed |

## Verification

- [x] Lint/document validation
- [x] Typecheck or Python compile
- [x] Unit/integration tests
- [x] Generator/generated-project E2E
- [x] Build/package validation
- [x] `git diff --check`
- [x] Documentation updated
- [ ] Independent specification review recorded
- [ ] Independent code-quality review recorded

## Review notes

- Independent specification and code-quality review will be requested on the pull request before merge.