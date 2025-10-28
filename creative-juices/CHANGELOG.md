# Changelog

All notable changes to the Creative Juices MCP server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-28

### Added
- Initial public release of Creative Juices MCP server
- HTTP-hosted server at `https://ai.yuda.me/mcp/creative-juices/serve`
- Three core tools for creative thinking:
  - `get_inspiration` - Gentle creative prompts with everyday metaphors
  - `think_outside_the_box` - Intense creative shocks for breakthrough thinking
  - `reality_check` - Strategic validation using Musk's frameworks
- 600+ curated words spanning human history:
  - Ancient tools and crafts
  - Medieval trades and architecture
  - Industrial revolution machinery
  - Modern technology and practices
- Strategic question library from four proven frameworks:
  - First Principles Thinking (6 questions)
  - Think in the Limit (6 questions)
  - Platonic Ideal (6 questions)
  - Five-Step Optimization (6 questions)
- One-click `.mcpb` bundle installation support
- Multi-client support:
  - Claude Desktop (macOS, Windows, Linux)
  - Claude Code CLI
  - Cursor
  - Windsurf
- Comprehensive documentation:
  - README with usage examples and design philosophy
  - INSTALLATION guide for all supported clients
  - Manifest file for MCP client discovery
  - CHANGELOG for version tracking

### Features
- No API keys or authentication required
- Zero external dependencies (uses Python stdlib `random`)
- Completely private - no data collection or logging
- Zero configuration needed - just add the URL
- True randomness using server-side seed rotation
- HTTP transport for universal client compatibility

### Technical Details
- Built with FastMCP framework
- Python 3.11+ backend
- Hosted on Django/Cuttlefish infrastructure
- Automatic health checks and status monitoring
- HTTPS for secure transport

---

## Future Roadmap

### Planned for 1.1.0
- [ ] Word list expansion (target: 1000+ words)
- [ ] Additional strategic frameworks from other thought leaders
- [ ] Language support (Spanish, French, German)
- [ ] Optional parameters for tool customization (e.g., number of prompts)
- [ ] Historical context annotations for words

### Under Consideration
- [ ] Custom word pool uploads (for domain-specific creativity)
- [ ] Weighted randomness (favor certain categories)
- [ ] Time-period filtering (e.g., "only medieval words")
- [ ] Cultural diversity tags for words
- [ ] API endpoint for programmatic access
- [ ] Analytics dashboard (aggregate usage stats, no user tracking)

### Community Requests
Have an idea? [Open an issue](https://github.com/yudame/ai-skills/issues) or submit a pull request!

---

## Version History

- **1.0.0** (2025-10-28) - Initial public release

---

**Note**: Prior to 1.0.0, Creative Juices was an internal tool in the Cuttlefish project. This is the first public release with HTTP hosting.
