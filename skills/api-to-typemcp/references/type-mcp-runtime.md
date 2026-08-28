# TypeMCP Runtime Contract

Generated projects use the reviewed public npm package on the current 0.4.0 release line:

```json
"@theorvane/type-mcp": "0.4.0"
```

`@theorvane/type-mcp@0.4.0` is published with npm registry `gitHead` and GitHub Release `v0.4.0` both resolving to `4141d25c287e57a76b905bd6f77c4681ab335378`.

## Allowed public API

The generator's default standard ESM path uses standard decorators from the public ESM/NodeNext entrypoint:

```ts
import { McpServer, McpTool } from "@theorvane/type-mcp";
```

Generated TypeScript uses only these public exports:

- `@McpServer`
- `@McpTool`
- `createMcpServer`
- `serveStdioServer`
- `zod`
- an explicit `InstanceResolver`

`createMcpServer` is asynchronous. Pass it through a fresh-server factory to `serveStdioServer`; the returned handle owns protocol negotiation and shutdown. Standard decorators use TC39 semantics: generated `tsconfig.json` must not enable legacy `experimentalDecorators` or `emitDecoratorMetadata`.

Contained MCP smoke verification imports the exact split SDK v2 client package, `@modelcontextprotocol/client@2.0.0`; generated runtime hosting remains owned by TypeMCP and its server dependency.

`@McpTool` requires an `input` Zod object. Generated code pins Zod v4 (`^4.4.3`) because that is the compatible public runtime contract for `@theorvane/type-mcp@0.4.0`.

## Legacy decorator compatibility

Standard and legacy decorators use distinct entrypoints and distinct decorator semantics. Legacy decorators are an opt-in public entrypoint for external CommonJS/Node16 projects that intentionally use TypeScript's legacy decorator mode; those projects must enable `experimentalDecorators` and import the decorators only from:

```ts
import { McpServer, McpTool } from "@theorvane/type-mcp/legacy";
```

Do not mix this entrypoint with the standard ESM/NodeNext imports. The generator does not copy TypeMCP runtime source and must remain on its default standard ESM path; do not change its templates to legacy decorators or CommonJS.

## Prohibited runtime boundaries

Never generate or publish any of the following:

- copied TypeMCP source code;
- `file:`, `git:`, `link:`, or `portal:` dependencies;
- imports from private, undocumented, or unavailable TypeMCP APIs;
- local TypeMCP checkouts as a generated-project dependency.

Before generated lifecycle scripts run, contained verification inspects dependency metadata and the generated `package-lock.json`, then runs `npm ci --ignore-scripts` in a fresh isolated workspace with inherited npm proxy configuration disabled. It then typechecks, tests, builds, and executes a local stdio smoke test against a mock upstream. Use a host container/VM/sandbox when the dependency graph is untrusted.
