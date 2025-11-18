# Example MCP Configurations

This directory contains ready-to-use MCP server configurations.

## Quick Copy

Copy any example to your MCP directories:

### User-level (available everywhere)

```bash
# Copy one
cp chrome-devtools.json ~/.claude/mcp-available/

# Copy multiple
cp web-search.json stripe.json postgres.json ~/.claude/mcp-available/
```

### Project-level (specific project only)

```bash
cd /path/to/your/project
mkdir -p ./mcp-available
cp ~/src/ai-skills/claude-code-mcp-selector/examples/sentry.json ./mcp-available/
```

## Available Examples

### chrome-devtools.json
Browser automation and DevTools access for Claude Code.

**Use for**: Web development, browser testing, UI debugging

### postgres.json
PostgreSQL database access.

**Use for**: Database queries, schema inspection, data analysis

**Note**: Update the connection string to match your database.

### stripe.json
Stripe API integration for payment processing.

**Use for**: Payment flows, subscription management, customer data

**Requires**: `STRIPE_SECRET_KEY` environment variable

### web-search.json
Web search capabilities.

**Use for**: Research, fact-checking, current information

### sentry.json
Sentry error tracking integration.

**Use for**: Bug investigation, error analysis, issue management

**Requires**:
- `SENTRY_AUTH_TOKEN` environment variable
- Update `SENTRY_ORG_SLUG` to your organization

**Project-specific**: Typically added to `./mcp-available/` per project

### linear.json
Linear issue tracking and project management.

**Use for**: Issue management, sprint planning, project tracking

**Requires**: `LINEAR_API_KEY` environment variable

**Project-specific**: Typically added to `./mcp-available/` per project

### render.json
Render cloud platform integration (HTTP transport).

**Use for**: Deployment management, service monitoring

**Project-specific**: Typically added to `./mcp-available/` per project

**Note**: No authentication required - uses HTTP transport

### creative-juices.json
Creative thinking prompts and strategic questions.

**Use for**: Brainstorming, problem-solving, strategic planning

## Customizing Examples

### Database Connection Strings

```json
{
  "postgres": {
    "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@host:port/dbname"]
  }
}
```

### Environment Variables

Set required environment variables before using:

```bash
export STRIPE_SECRET_KEY="sk_live_..."
export SENTRY_AUTH_TOKEN="sntrys_..."
```

Or add to your `~/.zshrc`:

```bash
echo 'export STRIPE_SECRET_KEY="sk_live_..."' >> ~/.zshrc
echo 'export SENTRY_AUTH_TOKEN="sntrys_..."' >> ~/.zshrc
source ~/.zshrc
```

## More MCP Servers

Browse the official MCP servers repository:
https://github.com/modelcontextprotocol/servers

Popular servers include:
- **GitHub**: Repository management
- **Slack**: Team communication
- **Gmail**: Email integration
- **Filesystem**: File operations
- **Memory**: Persistent storage
- **Puppeteer**: Browser automation
- **Brave Search**: Alternative search

## Creating Custom Configs

Template for new MCPs:

```json
{
  "server-name": {
    "command": "npx",
    "args": ["-y", "@package/mcp-server-name", "...args"],
    "env": {
      "VARIABLE_NAME": "${VARIABLE_NAME}"
    }
  }
}
```

1. Copy the template
2. Update `server-name`, package name, and args
3. Add required environment variables
4. Save to `~/.claude/mcp-available/your-server.json`
5. Test with `cc`

---

Need help? [Open an issue](https://github.com/yudame/ai-skills/issues)
