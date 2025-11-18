# Installation Guide

Quick setup guide for the Claude Code MCP Selector.

## Prerequisites

- **zsh** shell (default on macOS)
- **jq** for JSON processing
- **Claude Code** installed

### Install jq (if needed)

```bash
# macOS
brew install jq

# Linux (Ubuntu/Debian)
sudo apt-get install jq

# Linux (Fedora/RHEL)
sudo dnf install jq
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yudame/ai-skills.git ~/src/ai-skills
```

### 2. Add the function to your shell

```bash
cat ~/src/ai-skills/claude-code-mcp-selector/cc.zsh >> ~/.zshrc
source ~/.zshrc
```

### 3. Create MCP directories

```bash
# User-level MCPs (available everywhere)
mkdir -p ~/.claude/mcp-available

# Project-level MCPs (in your project)
cd /path/to/your/project
mkdir -p ./mcp-available
```

### 4. Add your first MCP

```bash
# Example: Add web-search to user MCPs
cat > ~/.claude/mcp-available/web-search.json << 'EOF'
{
  "web-search": {
    "command": "npx",
    "args": ["-y", "@anthropic/web-search"],
    "env": {}
  }
}
EOF
```

### 5. Test it

```bash
cc
```

You should see the interactive menu!

## Migrating Existing MCPs

If you already have MCPs configured in `~/.claude/mcp.json`, extract them to individual files:

```bash
# Example: Extract a single MCP
# From your existing mcp.json, copy just one server object:
cat > ~/.claude/mcp-available/postgres.json << 'EOF'
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"],
    "env": {}
  }
}
EOF
```

Repeat for each MCP you want to make selectable.

## Common MCP Configs

### Chrome DevTools

```bash
cat > ~/.claude/mcp-available/chrome-devtools.json << 'EOF'
{
  "chrome-devtools": {
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-server-chrome-devtools"],
    "env": {}
  }
}
EOF
```

### Stripe

```bash
cat > ~/.claude/mcp-available/stripe.json << 'EOF'
{
  "stripe": {
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-server-stripe"],
    "env": {
      "STRIPE_SECRET_KEY": "${STRIPE_SECRET_KEY}"
    }
  }
}
EOF
```

### PostgreSQL

```bash
cat > ~/.claude/mcp-available/postgres.json << 'EOF'
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/yourdb"],
    "env": {}
  }
}
EOF
```

### Context7

```bash
cat > ~/.claude/mcp-available/context7.json << 'EOF'
{
  "context7": {
    "transport": "sse",
    "url": "https://mcp.context7.com/sse"
  }
}
EOF
```

### Linear (Project-specific)

```bash
cd /path/to/your/project
mkdir -p ./mcp-available
cat > ./mcp-available/linear.json << 'EOF'
{
  "linear": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-linear"],
    "env": {
      "LINEAR_API_KEY": "${LINEAR_API_KEY}"
    }
  }
}
EOF
```

### Render (Project-specific)

```bash
cd /path/to/your/project
mkdir -p ./mcp-available
cat > ./mcp-available/render.json << 'EOF'
{
  "render": {
    "transport": "http",
    "url": "https://mcp.render.com/mcp"
  }
}
EOF
```

### Sentry (Project-specific)

```bash
cd /path/to/your/project
mkdir -p ./mcp-available
cat > ./mcp-available/sentry.json << 'EOF'
{
  "sentry": {
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-server-sentry"],
    "env": {
      "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
      "SENTRY_ORG_SLUG": "your-org-slug"
    }
  }
}
EOF
```

## Verification

### Check the function is loaded

```bash
type cc
# Should output: cc is a shell function...
```

### Check jq is working

```bash
jq --version
# Should output: jq-1.x
```

### Check Claude Code is in PATH

```bash
which claude
# Should output: /path/to/claude
```

### Test with a real launch

```bash
cd /path/to/your/project
cc
# Select an MCP and verify Claude Code launches
```

## Updating

To update to the latest version:

```bash
cd ~/src/ai-skills
git pull

# Re-add to shell (it will append, so remove old version first if needed)
# Or just source the new version
source ~/src/ai-skills/claude-code-mcp-selector/cc.zsh
```

## Uninstalling

To remove the `cc` function:

1. Edit `~/.zshrc`
2. Remove the section that starts with `# Claude Code MCP Selector`
3. Run `source ~/.zshrc`

The MCP config files in `~/.claude/mcp-available/` can be deleted if no longer needed.

## Troubleshooting

### "command not found: cc"

The function wasn't loaded. Run:
```bash
source ~/.zshrc
```

### "jq: command not found"

Install jq:
```bash
brew install jq  # macOS
```

### "No MCPs showing up"

Check files exist:
```bash
ls -la ~/.claude/mcp-available/
```

Verify JSON syntax:
```bash
jq . < ~/.claude/mcp-available/your-mcp.json
```

### "claude: command not found"

Claude Code isn't in your PATH. Check installation:
```bash
which claude
```

## Next Steps

- [Read the full README](./README.md) for usage examples
- Browse [available MCP servers](https://github.com/modelcontextprotocol/servers)
- Create project-specific configs in `./mcp-available/`

---

Need help? [Open an issue](https://github.com/yudame/ai-skills/issues)
