# Task brief: 94 — patch generated TypeMCP dependency resolutions

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/94
**Branch:** `fix/94-patch-generated-dependencies`
**Owner:** sjungwon03

## Goal

Generated TypeScript stdio projects deterministically resolve patched dependency versions for the current `fast-uri` and PostCSS advisories.

## Source references

- Runtime template: `skills/api-to-typemcp/templates/typescript-stdio/package.json.tmpl`
- Template lockfile: `skills/api-to-typemcp/templates/typescript-stdio/package-lock.json.tmpl`
- Verification contract: `skills/api-to-typemcp/tests/test_verify_generated_security.py`
- Dependabot alert #1: `fast-uri` high runtime (GHSA-7p8r-x3mc-p8w7)
- Dependabot alert #3: PostCSS medium development (GHSA-fxqj-rqcc-2cmp)

## Scope

### Included

- Patch the generated template lockfile's `fast-uri` resolution from 3.1.4 to 3.1.5.
- Add a deterministic security regression contract for the exact generated lockfile resolutions.
- Verify installation and generated-project behavior remain intact.

### Excluded

- Reviving the retired `packages/type-mcp-api-cli` package.
- Altering the published `@theorvane/type-mcp` runtime version.
- Unnecessary PostCSS churn: current template already resolves patched 8.5.24.

## Safety and contract notes

- Generated projects retain a deterministic npm lockfile and install through `npm ci --ignore-scripts` inside containment.
- `fast-uri` is transitive through the MCP SDK's AJV dependency; only the lock resolution changes.
- No credentials, release tags, external publishing, or API behavior changes are in scope.

## Test-first evidence

| Stage | Command | Expected/observed result |
| --- | --- | --- |
| Red | `python3.11 -m unittest skills.api-to-typemcp.tests.test_verify_generated_security -v` | Expected failure because template resolves vulnerable `fast-uri` 3.1.4. |
| Green | same command | Passed: 4 tests, including exact patched `fast-uri` and PostCSS template resolutions. |
| Regression | release/docs/workspace/E2E suites plus audit | Passed release/docs/workspace/E2E suites. Runtime audit confirms `fast-uri` is fixed; independent Hono moderate finding is tracked separately in #95. |

## Verification

- [x] Focused security contract
- [x] Release contract and documentation validation
- [x] Contained generated-project E2E
- [x] Template offline `npm ci --ignore-scripts`
- [x] `git diff --check`
- [x] Independent review

## Review notes

- Independent review requested stronger lockfile contract coverage; the test now asserts `fast-uri` version, registry URL, and SRI integrity.
- The template lockfile resolution was verified against the npm registry metadata and an isolated offline install.
- Runtime audit confirms `fast-uri` is remediated; remaining Hono moderate advisory is intentionally isolated in #95.