# Creative Juices MCP Server - Installation Guide

This guide covers installation for all MCP-compatible clients. The Creative Juices server is hosted at `https://ai.yuda.me/mcp/creative-juices/serve` - the processing happens on our servers, you just need a tiny proxy.

## One-Click Installation (Recommended)

The easiest way to install Creative Juices is using the MCP Bundle format:

1. **Download**: [creative-juices.mcpb](https://ai.yuda.me/mcp/creative-juices/download.mcpb)
2. **Install in Claude Desktop**:
   - Open Claude Desktop
   - Go to **Settings → Extensions** (or **Settings → Developer → Edit Config**)
   - Click **"Install from file..."** (or drag-and-drop the .mcpb file)
   - Select the downloaded `creative-juices.mcpb` file
3. **Restart Claude Desktop** (Cmd+Q then reopen, or Quit and restart)
4. **Verify**: Look for 🔨 icon in the Claude input area

**How it works**: The bundle contains a lightweight Node.js proxy (~60 lines) that forwards requests to our hosted server at ai.yuda.me. You get zero-config installation with automatic server-side updates.

**Bundle contents**:
- `manifest.json` - MCP metadata
- `client.js` - Node.js proxy (ships with Claude Desktop, no install needed)

**Compatible with**:
- ✅ Claude Desktop (macOS, Windows, Linux)
- ✅ Any MCP client supporting .mcpb bundles with Node.js runtime

If the one-click installation doesn't work, or you're using a different client, use the manual installation instructions below.

---

## Manual Installation by Client

<details>
<summary><strong>Claude Desktop</strong> (Click to expand)</summary>

### macOS

1. **Open config file**:
   ```bash
   code ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```
   Or use any text editor:
   ```bash
   open -a TextEdit ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. **Add Creative Juices server**:
   ```json
   {
     "mcpServers": {
       "creative-juices": {
         "url": "https://ai.yuda.me/mcp/creative-juices/serve"
       }
     }
   }
   ```

   If you already have other MCP servers configured, add `creative-juices` to the existing `mcpServers` object:
   ```json
   {
     "mcpServers": {
       "other-server": {
         "command": "node",
         "args": ["/path/to/other/server"]
       },
       "creative-juices": {
         "url": "https://ai.yuda.me/mcp/creative-juices/serve"
       }
     }
   }
   ```

3. **Save the file**

4. **Restart Claude Desktop**

5. **Verify installation**:
   - Look for a hammer icon (🔨) in the input area
   - Click it to see available tools
   - You should see: `get_inspiration`, `think_outside_the_box`, `reality_check`

### Windows

1. **Open config file**:
   ```
   %APPDATA%\Claude\claude_desktop_config.json
   ```
   Navigate to this path in File Explorer, or press `Win+R` and paste the path.

2. **Add Creative Juices server** (same JSON as macOS above)

3. **Save the file**

4. **Restart Claude Desktop**

### Linux

1. **Open config file**:
   ```bash
   code ~/.config/Claude/claude_desktop_config.json
   ```

2. **Add Creative Juices server** (same JSON as macOS above)

3. **Save the file**

4. **Restart Claude Desktop**

</details>

<details>
<summary><strong>Claude Code CLI</strong> (Click to expand)</summary>

The Claude Code CLI has a built-in command for adding MCP servers:

```bash
claude mcp add creative-juices --url https://ai.yuda.me/mcp/creative-juices/serve
```

**Verify installation**:
```bash
claude mcp list
```

You should see `creative-juices` in the list.

**Usage in Claude Code**:
When chatting with Claude, the tools will automatically be available. You can explicitly request them:
```
Use get_inspiration to help me brainstorm
```

**Remove if needed**:
```bash
claude mcp remove creative-juices
```

</details>

<details>
<summary><strong>Cursor</strong> (Click to expand)</summary>

1. **Open config file**:
   ```bash
   code ~/.cursor/mcp.json
   ```
   Or create it if it doesn't exist:
   ```bash
   mkdir -p ~/.cursor
   touch ~/.cursor/mcp.json
   ```

2. **Add Creative Juices server**:
   ```json
   {
     "mcpServers": {
       "creative-juices": {
         "url": "https://ai.yuda.me/mcp/creative-juices/serve"
       }
     }
   }
   ```

3. **Save the file**

4. **Restart Cursor**

5. **Verify installation**:
   Open Cursor's AI chat and try asking:
   ```
   Can you use get_inspiration to help me?
   ```

</details>

<details>
<summary><strong>Windsurf</strong> (Click to expand)</summary>

1. **Open config file**:
   ```bash
   code ~/.codeium/windsurf/mcp_config.json
   ```
   Or create it if it doesn't exist:
   ```bash
   mkdir -p ~/.codeium/windsurf
   touch ~/.codeium/windsurf/mcp_config.json
   ```

2. **Add Creative Juices server**:
   ```json
   {
     "mcpServers": {
       "creative-juices": {
         "url": "https://ai.yuda.me/mcp/creative-juices/serve"
       }
     }
   }
   ```

3. **Save the file**

4. **Restart Windsurf**

5. **Verify installation**:
   In Windsurf's AI assistant, try:
   ```
   Use think_outside_the_box to give me creative ideas
   ```

</details>

<details>
<summary><strong>Other MCP Clients</strong> (Click to expand)</summary>

Creative Juices works with any MCP client that supports HTTP transport. Consult your client's documentation for how to add MCP servers, and use:

**Server URL**: `https://ai.yuda.me/mcp/creative-juices/serve`

**Transport**: HTTP (not stdio)

**Authentication**: None required

**Configuration example** (may vary by client):
```json
{
  "url": "https://ai.yuda.me/mcp/creative-juices/serve",
  "transport": "http"
}
```

</details>

---

## Verification

After installation, verify the server is working by asking your AI assistant:

```
Can you list the available MCP tools?
```

You should see:
- **get_inspiration** - Generate 3 gentle verb-noun combinations for creative framing
- **think_outside_the_box** - Generate 3 intense verb-noun combinations for breaking linear thinking
- **reality_check** - Get strategic questions from Elon Musk's thinking frameworks

**Test a tool**:
```
Use get_inspiration to help me brainstorm
```

You should get a response with 3 random verb-noun combinations like "weave-tapestry", "kindle-ember", "harvest-meadow".

---

## Troubleshooting

### Tools not appearing

**Restart your client**: Most MCP clients only load server configurations on startup.

**Check config syntax**: Make sure your JSON is valid. Use [jsonlint.com](https://jsonlint.com) to validate.

**Check server URL**: It must be exactly `https://ai.yuda.me/mcp/creative-juices/serve` (no trailing slash).

**Check file location**: Make sure you're editing the right config file for your platform.

### Getting error messages

**Server might be down**: Check https://ai.yuda.me/mcp/creative-juices for status updates.

**HTTPS issues**: Some corporate networks block HTTPS requests. Try from a different network.

**Client compatibility**: Make sure your MCP client supports HTTP transport (not just stdio).

### Tools work but seem slow

**First call is slower**: The server might be cold-starting. Subsequent calls should be faster.

**Network latency**: HTTP MCP servers require network round-trips. This is normal.

### Need more help?

- **GitHub Issues**: https://github.com/yudame/ai-skills/issues
- **Website**: https://ai.yuda.me
- **Check status**: https://ai.yuda.me/mcp/creative-juices

---

## Uninstallation

To remove Creative Juices, simply delete the `creative-juices` entry from your MCP config file and restart your client.

**Claude Desktop / Cursor / Windsurf**:
1. Open your config file (see installation instructions above)
2. Remove the `"creative-juices": {...}` entry
3. Save the file
4. Restart your client

**Claude Code CLI**:
```bash
claude mcp remove creative-juices
```

---

## Next Steps

- **Read the README**: [README.md](./README.md) for usage examples and design philosophy
- **See what's new**: [CHANGELOG.md](./CHANGELOG.md) for version history
- **Try it out**: Start a conversation and use `get_inspiration` to break free from predictable thinking!

---

## About

Creative Juices is part of the Cuttlefish project by Tom Counsell. It's hosted at https://ai.yuda.me and maintained at https://github.com/yudame/cuttlefish.

**No tracking, no API keys, no cost. Just creative randomness whenever you need it.**
