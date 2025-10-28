# Creative Juices MCP Server

Break free from predictable AI responses with concrete, random creative prompts that span human history.

## What It Does

Creative Juices provides three tools that inject randomness into AI conversations to encourage divergent thinking:

1. **get_inspiration** - Gentle creative nudges using everyday verb-noun combinations (e.g., "weave-tapestry", "kindle-ember", "harvest-meadow")
2. **think_outside_the_box** - Intense creative shocks with dramatic combinations (e.g., "shatter-empire", "ignite-revolution", "demolish-fortress")
3. **reality_check** - Strategic validation questions from Elon Musk's proven thinking frameworks

Each tool returns randomized prompts drawn from a curated library of 600+ concrete words and strategic frameworks.

## Why Use This

**Break Habitual Thinking**: LLMs (and humans) tend to follow predictable patterns. Random concrete words force your AI assistant to make unexpected connections.

**No Setup Required**: Just add the server URL to your MCP client. No API keys, no authentication, no configuration.

**Completely Private**: All randomization happens server-side using Python's stdlib random module. No data is collected or transmitted.

**Historical Depth**: Words are deliberately drawn from across human history - ancient tools, medieval trades, industrial revolution, modern technology. This creates richer metaphors than contemporary-only vocabulary.

**Strategic Grounding**: The reality_check tool uses questions from four of Elon Musk's documented thinking frameworks to pressure-test ideas against first principles.

## Quick Start

**[→ Installation Guide](./INSTALLATION.md)** - One-click or manual installation for Claude Desktop, Claude Code, Cursor, and Windsurf

## Usage Examples

### Example 1: Feature Design

```
You: I need to design a new onboarding flow for our app
AI: Let me get some creative inspiration first...
[calls get_inspiration]
AI: Got these creative sparks: "weave-tapestry", "kindle-ember", "cultivate-garden"

Using these lenses:
- WEAVE-TAPESTRY: What if onboarding was about helping users weave their own story through your app, connecting different features like threads?
- KINDLE-EMBER: What if we focused on igniting just one "aha moment" rather than overwhelming with all features?
- CULTIVATE-GARDEN: What if onboarding was a patient process of helping users grow their understanding over time?

Which resonates with your product philosophy?
```

### Example 2: Breaking Through Writer's Block

```
You: I'm stuck writing this blog post about remote work
AI: Let's shake things up...
[calls think_outside_the_box]
AI: Here are some radical reframes: "shatter-empire", "ignite-rebellion", "demolish-cathedral"

- SHATTER-EMPIRE: What if remote work is actually destroying the empire of traditional office culture? Who are the winners and losers?
- IGNITE-REBELLION: What if you framed this as workers rebelling against pointless commutes and performative presence?
- DEMOLISH-CATHEDRAL: What if the office itself is a cathedral we built but no longer worship in?

Want to explore any of these angles?
```

### Example 3: Validating a Business Idea

```
You: I'm thinking of building a B2B SaaS for appointment scheduling
AI: That's a crowded space. Let me reality-check this idea...
[calls reality_check]
AI: Here are strategic questions from Musk's frameworks:

**First Principles**: "What's expensive: the materials or the manufacturing?"
- In scheduling software, what actually costs money? The code is written once. Is it really the product or the customer acquisition?

**Limit Thinking**: "What happens at 1 unit vs 1 million units?"
- At 1 customer, you can do white-glove service. At 1M customers, what breaks? Support? Infrastructure? Your current approach?

**Platonic Ideal**: "If you designed this from scratch today, what would it be?"
- Ignoring Calendly and others, what would perfect scheduling look like? Maybe it's not even software?

**Optimization**: "What steps can be eliminated entirely?"
- Does scheduling need to exist at all? What if meetings could self-organize based on availability APIs?

These questions suggest you might be solving the wrong problem or entering a commoditized market. What makes your approach different?
```

### Example 4: Mid-Conversation Reset

```
You: We've been going in circles on this API design for 20 minutes
AI: You're right, we're stuck in linear thinking. Let me break us out...
[calls think_outside_the_box]
AI: Fresh perspective: "resurrect-phoenix", "forge-blade", "summon-storm"

We've been optimizing the existing structure. What if we:
- RESURRECT-PHOENIX: Burn it down and rebuild from the ashes with what we learned?
- FORGE-BLADE: Focus on making one endpoint razor-sharp instead of a Swiss Army knife API?
- SUMMON-STORM: Create something so different it disrupts how people think about this problem?

Which direction feels right?
```

## Tool Reference

### get_inspiration

**When to use**: At the start of creative tasks or when you need gentle reframing.

**What it returns**:
```json
{
  "sparks": ["weave-tapestry", "kindle-ember", "harvest-meadow"],
  "instruction": "Use these unexpected combinations as initial lenses:"
}
```

**Tone**: Gentle, constructive, nurturing. Uses verbs like "weave", "kindle", "cultivate" paired with natural/traditional nouns.

**Best for**:
- Initial brainstorming
- Design problems
- Content ideation
- Feature planning

---

### think_outside_the_box

**When to use**: Mid-conversation when thinking has become linear or you're stuck in a rut.

**What it returns**:
```json
{
  "sparks": ["shatter-empire", "ignite-revolution", "demolish-fortress"],
  "instruction": "Shatter your assumptions with these:"
}
```

**Tone**: Intense, disruptive, dramatic. Uses verbs like "shatter", "demolish", "ignite" paired with powerful/historical nouns.

**Best for**:
- Breaking creative blocks
- Challenging assumptions
- Radical reframing
- When safe ideas aren't working

---

### reality_check

**When to use**: When wild ideas need pressure-testing or you need strategic grounding.

**What it returns**:
```json
{
  "questions": [
    "What are the absolute truths here, known by physics?",
    "What happens at 1 unit vs 1 million units?",
    "What does the perfect version of this look like?",
    "What can you remove? Are you adding things 'just in case'?"
  ],
  "frameworks": [
    "first_principles",
    "limit_thinking",
    "platonic_ideal",
    "optimization"
  ],
  "instruction": "Ground your thinking with one question from each Musk framework:"
}
```

**Frameworks**:
1. **First Principles Thinking** - Strip to fundamental truths, remove assumptions
2. **Think in the Limit** - Scale to extremes (1x vs 1,000,000x)
3. **Platonic Ideal** - Work backwards from perfection
4. **Five-Step Optimization** - Question, delete, optimize, accelerate, automate

**Best for**:
- Validating business ideas
- Pressure-testing technical decisions
- Identifying what actually matters
- Cutting through complexity

## Design Philosophy

### Why Concrete Words?

Abstract words like "innovation" or "synergy" are vague - they allow AI to fall back into familiar patterns. Concrete words like "forge", "cathedral", "tapestry" force specific imagery and unexpected connections.

This is based on research showing concrete nouns activate different neural pathways than abstract concepts, creating stronger creative friction.

### Why Three Tools?

Each tool serves a distinct phase of creative work:
1. **get_inspiration** - Divergent opening (explore possibilities)
2. **think_outside_the_box** - Divergent breakthrough (escape ruts)
3. **reality_check** - Convergent validation (ground in reality)

Having three tools gives AI assistants the metacognitive ability to choose the right intervention based on conversation context.

### Why Historical Words?

Modern vocabulary is dominated by digital metaphors (upload, download, sync, cloud). Historical words (forge, cathedral, harvest, siege) connect to deeper human experiences across millennia.

This creates richer, more resonant metaphors that work across cultures and contexts.

### Why Musk's Frameworks?

These frameworks are documented in public interviews and have been used to solve massive real-world problems (reusable rockets, electric vehicles, tunnel boring). They're proven, not theoretical.

The reality_check tool doesn't prescribe answers - it asks strategic questions that help users think more clearly.

## Technical Details

**Language**: Python 3.11+
**Protocol**: Model Context Protocol (MCP) over HTTP
**Framework**: FastMCP
**Hosting**: https://ai.yuda.me/mcp/creative-juices/serve
**Dependencies**: None (uses Python stdlib `random`)
**Authentication**: None required
**Data Collection**: None
**Rate Limiting**: None (feel free to spam it)

**Privacy**: All randomization happens server-side. The server receives no information about your conversation - tools take no parameters. Nothing is logged except basic health metrics.

**Source Code**: Available in the [Cuttlefish project](https://github.com/yudame/cuttlefish/blob/main/apps/ai/mcp/creative_juices_server.py) (private repo, but code is visible).

## Compatibility

Works with any MCP-compatible client:
- ✅ Claude Desktop (macOS, Windows, Linux)
- ✅ Claude Code CLI
- ✅ Cursor
- ✅ Windsurf
- ✅ Any MCP client supporting HTTP transport

## Limitations

**Randomness is Truly Random**: You can't control which words appear. Sometimes you get perfect metaphors, sometimes you get weird ones. That's the point - embrace the chaos.

**No Context Awareness**: Tools don't know what you're working on. They just return random prompts. It's up to you (and your AI assistant) to make meaningful connections.

**English Only**: All words and frameworks are in English. Future versions may include other languages.

**Limited Word Pool**: 600+ words is a lot, but you might see repeats in long sessions. The randomness ensures each combination is still unique.

## Troubleshooting

**Tools not appearing in my client?**
- Make sure you restarted your client after adding the server
- Check that the URL is exactly: `https://ai.yuda.me/mcp/creative-juices/serve`
- Some clients require server health checks - this server responds to standard MCP health pings

**Getting errors when calling tools?**
- The server might be temporarily down. Check https://ai.yuda.me/mcp/creative-juices for status
- Report persistent issues at https://github.com/yudame/ai-skills/issues

**Words seem repetitive?**
- The random seed resets server-side periodically for true randomness
- You're more likely to notice repeats when using tools frequently
- Consider it a feature - sometimes the same word in different combinations reveals new meaning

## Version History

See [CHANGELOG.md](./CHANGELOG.md) for detailed version history.

## Links

- **Landing Page**: https://ai.yuda.me/mcp/creative-juices
- **Installation Guide**: [INSTALLATION.md](./INSTALLATION.md)
- **HTTP Endpoint**: https://ai.yuda.me/mcp/creative-juices/serve
- **Manifest**: https://ai.yuda.me/mcp/creative-juices/manifest.json
- **Download Bundle**: https://ai.yuda.me/mcp/creative-juices/download.mcpb

## Support

- **Issues**: https://github.com/yudame/ai-skills/issues
- **Website**: https://ai.yuda.me
- **Email**: Available on website

## License

Part of the Cuttlefish project. See [LICENSE](../LICENSE) for details.
