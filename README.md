# Yuda AI Skills & MCP Servers

Documentation and resources for AI tools from [ai.yuda.me](https://ai.yuda.me)

**⚠️ MCPB Bundle Issue**: One-click installation currently has a version compatibility warning (requires Claude Desktop 1.0.0+, but latest is 0.14.x). Use manual installation for now. [See troubleshooting →](./TROUBLESHOOTING.md)

## Creative Juices MCP Server

**HTTP-hosted MCP server** for creative thinking and strategic validation. No installation, no API keys, just add a URL.

**Quick Start**: Add to your MCP client:
```
https://ai.yuda.me/mcp/creative-juices/serve
```

**Three Tools**:
- `get_inspiration` - Gentle creative nudges with concrete metaphors
- `think_outside_the_box` - Intense creative shocks for breakthrough thinking
- `reality_check` - Strategic questions from Musk's frameworks

**[→ Full Documentation](./creative-juices/README.md)** | **[→ Installation Guide](./creative-juices/INSTALLATION.md)**

---

## Claude Code MCP Selector

**Interactive shell function** for selectively loading MCP servers before launching Claude Code.

**Quick Start**: Install and use:
```bash
cat ~/src/ai-skills/claude-code-mcp-selector/cc.zsh >> ~/.zshrc
source ~/.zshrc
cc
```

**Key Features**:
- 📋 Interactive menu showing all available MCPs
- 🎯 Load only what you need for each session
- 🏢 User-level + project-level MCP configs
- ⚡ Fast selection via numbers or shortcuts
- 🔒 Control permission prompts (--dangerously-skip-permissions)

**Why use it?**: Instead of loading all MCPs every time, pick exactly what you need. Faster launches, cleaner sessions, project-specific tooling.

**[→ Full Documentation](./claude-code-mcp-selector/README.md)** | **[→ Installation Guide](./claude-code-mcp-selector/INSTALLATION.md)**

---

## About This Repository

This repository contains documentation and utilities for AI tools:

- **Creative Juices MCP Server**: HTTP-hosted MCP for creative thinking and strategic validation
- **Claude Code MCP Selector**: Interactive shell function for managing MCP configurations

More tools coming soon!

## Features

- **No Setup**: HTTP-hosted, just add a URL to your MCP client config
- **No API Keys**: Completely open, no authentication required
- **No Tracking**: Zero data collection, complete privacy
- **600+ Words**: Curated vocabulary spanning human history
- **Proven Frameworks**: Strategic questions from Elon Musk's documented thinking methods
- **Multi-Client**: Works with Claude Desktop, Claude Code, Cursor, Windsurf, and any MCP client

## Why Creative Juices?

LLMs and humans both fall into predictable patterns. Random concrete words force unexpected connections. Strategic questions pressure-test assumptions. Together, they help break free from habitual thinking.

Read more in the [design philosophy](./creative-juices/README.md#design-philosophy).

## Installation

**One-click**: Download [creative-juices.mcpb](https://ai.yuda.me/mcp/creative-juices/download.mcpb)

**Manual**: Add this to your MCP client config:
```json
{
  "mcpServers": {
    "creative-juices": {
      "url": "https://ai.yuda.me/mcp/creative-juices/serve"
    }
  }
}
```

See [INSTALLATION.md](./creative-juices/INSTALLATION.md) for detailed instructions for each client.

## Testing & Verification

[![MCP Server Tests](https://github.com/yudame/ai-skills/actions/workflows/test-mcp-servers.yml/badge.svg)](https://github.com/yudame/ai-skills/actions/workflows/test-mcp-servers.yml)

**✅ 12/12 tests passing** - Open source tests prove our servers work as documented.

```bash
# Run tests locally
pip install -r tests/requirements.txt
pytest tests/test_creative_juices.py -v
```

- **Automated Testing**: GitHub Actions runs tests every 6 hours
- **Production Validation**: Tests run against live servers at ai.yuda.me
- **Public Transparency**: All test code is open source
- **100% Success Rate**: All MCP protocol compliance and tool tests passing

See [tests/README.md](./tests/README.md) for detailed testing documentation and [FINDINGS.md](./FINDINGS.md) for validation report.

## Roadmap

### Completed
- [x] Comprehensive documentation
- [x] 600+ curated words across history
- [x] Four strategic frameworks (24 questions)
- [x] Multi-client installation guides
- [x] Automated test suite
- [x] CI/CD monitoring pipeline

### In Progress
- [ ] Deploy HTTP-hosted MCP server to production
- [ ] Finalize server endpoint architecture
- [ ] User feedback collection
- [ ] Word list expansion (target: 1000+)

### Future
- [ ] QuickBooks MCP server documentation
- [ ] Language support (Spanish, French, German)
- [ ] Additional MCP tools and servers

## Contributing

We welcome contributions! Areas for improvement:

- **Word lists**: Add more words, new categories, cultural diversity
- **New skills**: Propose new specialized tasks
- **Examples**: Real-world usage patterns
- **Frameworks**: Additional strategic thinking frameworks

## Links

- **Website**: https://ai.yuda.me
- **Main project**: https://github.com/tomcounsell/cuttlefish
- **MCP servers**: https://github.com/tomcounsell/cuttlefish/tree/main/apps/ai/mcp

## License

MIT License - See LICENSE file for details

---

**Questions or feedback?** Open an issue or reach out at https://ai.yuda.me
