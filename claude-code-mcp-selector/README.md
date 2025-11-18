# Claude Code MCP Selector (`cc`)

**Interactive shell function** for selecting which MCP servers to load before launching Claude Code.

## Why?

Claude Code loads all MCPs from `~/.claude/mcp.json` on every launch. This can be:
- **Slow** when you have many MCPs installed
- **Wasteful** when you only need 1-2 for your current task
- **Inflexible** when different projects need different MCPs

The `cc` function solves this by:
- Showing you a menu of available MCPs
- Letting you pick exactly what you need
- Building the config file on-the-fly
- Launching Claude Code with your selection

## Features

✅ **Clean terminal UI** with visual menu
✅ **User-level MCPs** (available everywhere)
✅ **Project-level MCPs** (only in specific directories)
✅ **Project override protection** (blocks parent configs)
✅ **Single-line selection** (numbers, flags, all in one)
✅ **Permission control** (add 'n' to require permissions)
✅ **Fast selection** via numbers or shortcuts
✅ **Pass-through args** to Claude Code

## Quick Start

### 1. Install the function

```bash
# Clone this repo (if you haven't already)
git clone https://github.com/yudame/ai-skills.git ~/src/ai-skills

# Add to your shell
cat ~/src/ai-skills/claude-code-mcp-selector/cc.zsh >> ~/.zshrc
source ~/.zshrc
```

### 2. Create MCP config directories

```bash
# User-level MCPs (available in all projects)
mkdir -p ~/.claude/mcp-available

# Project-level MCPs (optional, per project)
mkdir -p ./mcp-available
```

### 3. Add your MCPs

Each `.json` file contains one MCP server config:

```bash
# Example: Desktop Commander (user-level)
cat > ~/.claude/mcp-available/desktop-commander.json << 'EOF'
{
  "desktop-commander": {
    "command": "npx",
    "args": ["-y", "@anthropic/desktop-commander"],
    "env": {}
  }
}
EOF

# Example: Sentry (project-level)
mkdir -p ./mcp-available
cat > ./mcp-available/sentry.json << 'EOF'
{
  "sentry": {
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-server-sentry"],
    "env": {
      "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
      "SENTRY_ORG_SLUG": "your-org"
    }
  }
}
EOF
```

### 4. Launch with selection

```bash
cc
```

You'll see:
```
╭─────────────────────────────╮
│     Claude Code MCPs        │
╰─────────────────────────────╯

  e) empty (no MCPs)
  a) all
  n) require permissions (default: skip)

User:
   1) chrome-devtools
   2) context7
   3) postgres
   4) stripe
   5) web-search

Project:
   6) linear
   7) render
   8) sentry

────────────────────────────────
Select (space-separated): 3 8

→ Loading: postgres sentry
→ Skipping permissions
```

## Usage

### Single-Line Selection

Everything is selected in one prompt:

**Numbers**: Select specific MCPs (default: skip permissions)
```
Select: 1 3 5
→ Loading: chrome-devtools postgres sentry
→ Skipping permissions
```

**With 'n' flag**: Require permissions
```
Select: 1 3 5 n
→ Loading: chrome-devtools postgres sentry
→ Requiring permissions
```

**Empty (`e`)**: No MCPs
```
Select: e
→ Running empty (no MCPs)
→ Skipping permissions
```

**All (`a`)**: Load everything
```
Select: a
→ Loading: chrome-devtools context7 postgres stripe web-search linear render sentry
→ Skipping permissions
```

**All with permissions**:
```
Select: a n
→ Loading: chrome-devtools context7 postgres stripe web-search linear render sentry
→ Requiring permissions
```

### Pass-through Arguments

The function passes any arguments to `claude`:

```bash
cc --help                    # Show Claude Code help
cc --version                 # Show version
cc /path/to/project          # Open specific project
```

## Directory Structure

```
~/.claude/
├── mcp.json              # Active config (auto-generated)
└── mcp-available/        # User-level MCP configs
    ├── chrome-devtools.json
    ├── postgres.json
    ├── stripe.json
    └── web-search.json

./mcp-available/          # Project-level MCP configs
    └── sentry.json
```

## Config File Format

Each `.json` file contains a single MCP server object:

```json
{
  "server-name": {
    "command": "npx",
    "args": ["-y", "@package/name"],
    "env": {
      "VAR_NAME": "${ENV_VAR}"
    }
  }
}
```

The object key becomes the server name in the final config.

## How It Works

1. **Scans** `~/.claude/mcp-available/` and `./mcp-available/` for `.json` files
2. **Displays** interactive menu with all available MCPs
3. **Parses** selection for MCPs and 'n' flag (permissions)
4. **Writes** selected configs to `~/.claude/mcp.json`
5. **Writes** empty `./.mcp.json` to block parent project configs
6. **Launches** `claude` with optional `--dangerously-skip-permissions` flag

### Project Override Protection

The function writes an empty `./.mcp.json` in the current directory to prevent Claude Code from loading MCPs from parent directories. This ensures **only** your selected MCPs load, even if you're in a subdirectory of a project with its own MCP config.

## Example Configs

### Chrome DevTools
```json
{
  "chrome-devtools": {
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-server-chrome-devtools"],
    "env": {}
  }
}
```

### PostgreSQL
```json
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"],
    "env": {}
  }
}
```

### Stripe
```json
{
  "stripe": {
    "command": "npx",
    "args": ["-y", "@anthropic/mcp-server-stripe"],
    "env": {
      "STRIPE_SECRET_KEY": "${STRIPE_SECRET_KEY}"
    }
  }
}
```

### Context7
```json
{
  "context7": {
    "transport": "sse",
    "url": "https://mcp.context7.com/sse"
  }
}
```

### Linear (Project-specific)
```json
{
  "linear": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-linear"],
    "env": {
      "LINEAR_API_KEY": "${LINEAR_API_KEY}"
    }
  }
}
```

### Render (Project-specific)
```json
{
  "render": {
    "transport": "http",
    "url": "https://mcp.render.com/mcp"
  }
}
```

### Sentry (Project-specific)
```json
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
```

**Note**: Project-specific MCPs (Linear, Render, Sentry) are typically added to `./mcp-available/` in each project directory rather than `~/.claude/mcp-available/`.

## Troubleshooting

### `jq` not found
```bash
brew install jq
```

### MCPs not showing up
- Check `.json` files exist in correct directories
- Verify JSON syntax: `jq . < file.json`
- Ensure filenames end with `.json`

### Claude Code not launching
- Verify installation: `which claude`
- Check PATH includes Claude Code binary

### Permission issues
If you get permission errors:
- Try without skip: Add `n` to your selection (e.g., `2 5 n`)
- Check MCP server has correct permissions
- Verify environment variables are set

### Parent project configs loading
If you see MCPs you didn't select:
- Check for `.mcp.json` files in parent directories
- The function writes `./.mcp.json` to block them
- Delete or move old project configs if needed

## Advanced Usage

### Multiple Projects

Each project can have its own MCPs:

```bash
# Project A
cd ~/projects/web-app
mkdir -p mcp-available
cat > mcp-available/chrome.json << 'EOF'
{"chrome-devtools": {...}}
EOF

# Project B
cd ~/projects/data-analysis
mkdir -p mcp-available
cat > mcp-available/postgres.json << 'EOF'
{"postgres": {...}}
EOF
```

### Override User MCPs

Project configs override user configs with the same name:

```
~/.claude/mcp-available/postgres.json  → Database A
./mcp-available/postgres.json          → Database B (wins!)
```

### Workflow Example

```bash
# Daily workflow
cd ~/projects/web-app

# Quick debugging session (no MCPs)
cc
Select: n

# Full-stack development
cc
Select: 1 3 5  # chrome-devtools, postgres, sentry
Skip permissions? [Y/n]:

# Data analysis
cc
Select: 2  # just postgres
Skip permissions? [Y/n]: n  # require permissions
```

## Requirements

- **zsh** shell (comes with macOS)
- **jq** for JSON merging (`brew install jq`)
- **Claude Code** installed and in PATH

## License

MIT License - See [LICENSE](../LICENSE) file for details

## Links

- **Main repo**: https://github.com/yudame/ai-skills
- **MCP Documentation**: https://modelcontextprotocol.io
- **Claude Code**: https://claude.ai/code

---

**Questions or feedback?** Open an issue at https://github.com/yudame/ai-skills/issues
