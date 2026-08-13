# Task brief: 95 — update generated Hono runtime resolution

**Status:** in-progress
**Issue:** https://github.com/Theorvane/type-mcp-api-agent-skill/issues/95
**Branch:** `fix/95-patch-generated-hono`
**Owner:** sjungwon03

## Goal

Generated TypeScript stdio projects deterministically resolve a Hono version patched for current runtime advisories.

## Source references

- Runtime template: `skills/api-to-typemcp/templates/typescript-stdio/package.json.tmpl`
- Template lockfile: `skills/api-to-typemcp/templates/typescript-stdio/package-lock.json.tmpl`
- Verification contract: `skills/api-to-typemcp/tests/test_verify_generated_security.py`
- Issue: https://github.com/Theorvane/type-mcp-api-agent-skill/issues/95

## Scope

### Included

- Update the active generated-project lockfile Hono resolution from 4.12.32 to patched 4.12.34.
- Add deterministic version/registry URL/SRI regression coverage.
- Verify contained install, audit, and generated-project E2E.

### Excluded

- Releasing a new skill version or modifying existing releases/tags.
- Changing the published TypeMCP runtime dependency.
- Reopening or changing the completed fast-uri remediation in #94.

## Safety and contract notes

- Hono is transitive through the published MCP SDK and compatible with its `^4.11.4` dependency requirement and `@hono/node-server` peer requirement `^4`.
- Generated project installation remains contained with `npm ci --ignore-scripts`.
- No credentials or external publication actions are in scope.

## Test-first evidence

| Stage | Command | Expected/observed result |
| --- | --- | --- |
| Red | `python3.11 -m unittest skills.api-to-typemcp.tests.test_verify_generated_security -v` | Observed expected failure: `AssertionError: '4.12.32' != '4.12.34'` in the Hono lock-resolution contract. |
| Green | same command | Passed: 4 focused security-contract tests, including exact Hono version, registry URL, and SRI. |
| Regression | contained install/audit and E2E suites | Passed: rendered template installed with `npm ci --ignore-scripts`; production audit reported 0 vulnerabilities; release/docs/workspace and contained E2E suites passed. |

## Verification

- [x] Focused security contract
- [x] Template install and production audit
- [x] Release/docs/workspace validation
- [x] Contained generated-project E2E
- [x] `git diff --check`
- [x] Independent review

## Review notes

- The resolution is compatible with MCP SDK `hono ^4.11.4`, `@hono/node-server` peer `^4`, and Node `>=16.9.0`.
- The template now installs `hono 4.12.34`; its production audit reports 0 vulnerabilities.