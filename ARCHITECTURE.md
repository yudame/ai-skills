# MCP Server Architecture

## Overview

Yuda AI MCP servers use a **hybrid hosted architecture** that combines the benefits of cloud hosting with the convenience of one-click MCPB bundle installation.

## Architecture Diagram

```
┌─────────────────┐
│  Claude Desktop │
│                 │
│  [User Types]   │
└────────┬────────┘
         │
         │ (stdio: stdin/stdout)
         │
    ┌────▼────┐
    │ client.js│ ◄─── Installed via .mcpb bundle
    │ (Node.js)│      (~60 lines, runs locally)
    └────┬────┘
         │
         │ (HTTPS POST)
         │
    ┌────▼────────────────────────┐
    │ https://ai.yuda.me          │
    │ /mcp/creative-juices/serve  │
    │                             │
    │ Django + FastMCP Server     │
    │ (Python 3.11+)              │
    └─────────────────────────────┘
```

## Components

### 1. Client Proxy (client.js)

**Location**: Bundled in `.mcpb` file, extracted by Claude Desktop

**Function**: Lightweight proxy that bridges MCP protocol over stdio to HTTP

**Implementation**:
```javascript
// Reads JSON-RPC from stdin
process.stdin.on('data', (chunk) => {
  // Forwards to hosted server via HTTPS POST
  https.request(HOSTED_URL, (res) => {
    // Writes response back to stdout
    process.stdout.write(responseData);
  });
});
```

**Size**: ~60 lines of vanilla Node.js (no dependencies)

**Runtime**: Uses Node.js bundled with Claude Desktop (no user installation needed)

### 2. Hosted Server

**Location**: https://ai.yuda.me/mcp/creative-juices/serve

**Stack**:
- **Web Server**: Gunicorn behind Cloudflare
- **Framework**: Django 4.x
- **MCP Implementation**: FastMCP library
- **Language**: Python 3.11+

**Endpoints**:
- `POST /mcp/creative-juices/serve` - MCP JSON-RPC endpoint
- `GET /mcp/creative-juices/download.mcpb` - Bundle download

**Processing**:
1. Receives JSON-RPC 2.0 requests
2. Routes to appropriate MCP tool handler
3. Generates random creative prompts (using stdlib `random`)
4. Returns JSON-RPC 2.0 response

## MCPB Bundle Format

### Contents

```
creative-juices.mcpb (zip archive)
├── manifest.json    # MCP metadata
└── client.js        # Node.js proxy
```

### Manifest Structure

```json
{
  "manifest_version": "0.3",
  "name": "creative-juices",
  "version": "1.0.0",
  "server": {
    "type": "node",
    "entry_point": "client.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/client.js"]
    }
  }
}
```

### Installation Flow

1. **User downloads** `.mcpb` from ai.yuda.me
2. **User installs** in Claude Desktop (Settings → Extensions → Install from file)
3. **Claude Desktop**:
   - Extracts `.mcpb` (it's a zip file)
   - Reads `manifest.json`
   - Validates `server.type === "node"`
   - Executes `node ${__dirname}/client.js` as subprocess
4. **Client proxy** starts, listens on stdin, connects to hosted server
5. **Ready**: Tools appear in Claude Desktop

## Why This Architecture?

### Problem We Solved

**MCPB bundles can't directly reference HTTP endpoints**. They must bundle executable code:
- ✅ `python` - Bundle Python scripts
- ✅ `node` - Bundle Node.js scripts
- ✅ `binary` - Bundle compiled executables
- ❌ `http` - NOT supported (Invalid enum value error)

### Our Solution

Bundle a **tiny proxy** that:
1. Satisfies MCPB requirements (bundles Node.js code)
2. Connects to hosted server (gets cloud benefits)
3. Requires zero user dependencies (Node.js ships with Claude Desktop)

### Benefits

**For Users**:
- ✅ One-click installation (no config editing)
- ✅ Zero dependencies (Node.js pre-installed)
- ✅ Automatic updates (server-side deployments)
- ✅ Works offline (could add local fallback)

**For Developers**:
- ✅ Deploy updates without user action
- ✅ Centralized monitoring and analytics
- ✅ No client code maintenance (proxy never changes)
- ✅ Scale server independently

**For Open Source**:
- ✅ Proxy code is tiny and auditable (~60 lines)
- ✅ Server code is open (GitHub: yudame/cuttlefish)
- ✅ No black box executables
- ✅ Full transparency

## Installation Methods Comparison

| Method | User Experience | Update Process | Dependencies |
|--------|----------------|----------------|--------------|
| **MCPB Bundle** | One-click install | Server-side (instant) | None (Node.js bundled) |
| **Direct HTTP** | Edit JSON config | Server-side (instant) | None |
| **Local Execution** | Download + setup | User must update | Python 3.11+ |

## Security & Privacy

### Data Flow

```
User input → Claude Desktop → client.js (local) → HTTPS → Server
                                                         ↓
User sees response ← Claude Desktop ← client.js ← JSON-RPC Response
```

### What We Collect

**Nothing**. The server:
- ✅ Receives no conversation context
- ✅ Tools take zero parameters
- ✅ Only logs: request count, response time (aggregate metrics)
- ✅ No IP logging, no user tracking, no analytics

### Verification

Users can verify:
1. **Proxy code**: Inspect `client.js` from extracted `.mcpb`
2. **Server code**: Review on [GitHub](https://github.com/yudame/cuttlefish/tree/main/apps/ai/mcp)
3. **Network traffic**: Monitor HTTPS requests (only goes to ai.yuda.me)

## Testing & Validation

### Open-Source Test Suite

Location: `tests/test_creative_juices.py`

Tests verify:
- Server health and reachability
- MCP protocol compliance
- All tool endpoints functional
- Performance benchmarks (<5s response time)
- Error handling

**Current Status**: ✅ 12/12 tests passing

Run tests:
```bash
pip install -r tests/requirements.txt
pytest tests/test_creative_juices.py -v
```

### Continuous Monitoring

- **GitHub Actions**: Runs tests every 6 hours
- **Status Badge**: Displays in README
- **Public Results**: All test runs visible on GitHub

## Deployment

### Server Deployment

**Platform**: Render.com (Django app)

**Process**:
1. Push to `main` branch on GitHub
2. Render auto-deploys
3. Django server restarts
4. Changes live in ~2 minutes
5. No client updates needed

### Bundle Distribution

**URL**: `https://ai.yuda.me/mcp/creative-juices/download.mcpb`

**Generation**:
```bash
cd apps/ai/mcp/bundles
./build.sh creative-juices
```

**Deployment**:
- Bundle served by Django static files
- Cloudflare CDN caching
- Downloads from ai.yuda.me

## Future Enhancements

### Potential Improvements

1. **Offline Fallback**: Bundle word lists in .mcpb, use local if server unreachable
2. **Caching**: Client could cache previous responses
3. **Compression**: gzip responses from server
4. **Load Balancing**: Multiple server instances if needed
5. **Regional Servers**: CDN-like distribution for lower latency

### Maintaining Simplicity

Key principle: **Keep proxy minimal**
- Proxy should never need updates
- All logic lives server-side
- Bundle stays small and auditable

## References

- **MCP Specification**: https://modelcontextprotocol.io
- **FastMCP Library**: https://github.com/jlowin/fastmcp
- **MCPB Format**: https://modelcontextprotocol.io/docs/tools/bundles
- **Source Code**: https://github.com/yudame/cuttlefish/tree/main/apps/ai/mcp

---

**Questions?** Open an issue at https://github.com/yudame/ai-skills/issues
