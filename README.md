# Yuda AI Skills

Official collection of Claude Skills from [Yuda.me](https://ai.yuda.me)

## What Are Skills?

Skills are reusable, file-based instructions that teach Claude specialized tasks. They're token-efficient (only ~30-50 tokens for discovery) and work across Claude.ai, API, and Claude Code.

## Installation

### Quick Install

```bash
/plugin marketplace add yudame/ai-skills
/plugin install creative-juices
```

### Manual Install

1. Clone this repository
2. Copy the skill folder to `~/.claude/skills/`
3. Restart Claude

## Available Skills

### Creative Juices

**Status:** ✅ Ready to use

Break free from predictable AI responses with randomized creative prompts.

**Use when:**
- Need inspiration or fresh perspectives
- Stuck on design/feature problems
- Want to validate assumptions or reality-check ideas

**Three tools:**
1. `get_inspiration` - Gentle creative nudges with everyday metaphors
2. `think_outside_the_box` - Intense creative shocks with dramatic scenarios
3. `reality_check` - Strategic validation using Elon Musk's frameworks

[Full documentation →](./creative-juices/SKILL.md)

## Development Status

Creative Juices skill is complete and ready for use! The skill is based on the MCP server implementation at [cuttlefish/apps/ai/mcp/creative_juices_server.py](https://github.com/tomcounsell/cuttlefish/blob/main/apps/ai/mcp/creative_juices_server.py).

## Roadmap

- [x] Repository structure
- [x] Marketplace manifest
- [x] Creative Juices skill with complete implementation
- [x] Word list supporting files (1,100+ words)
- [x] Framework reference documentation (24 questions)
- [x] Comprehensive usage examples
- [ ] Test installation and gather user feedback
- [ ] Host marketplace.json at https://ai.yuda.me/skills/marketplace.json
- [ ] Future skills: QuickBooks assistant, documentation helper, etc.

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
