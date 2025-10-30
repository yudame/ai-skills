# Troubleshooting Guide

Common issues and solutions for Yuda AI MCP servers.

## MCPB Bundle Installation Issues

### ❌ "Requires Claude Desktop >=1.0.0" Error

**Symptom**: When installing `.mcpb` bundle, you see:
```
Requirements
an update to Claude Desktop
darwin
Claude Desktop >=1.0.0
Node.js >=16.0.0
This extension may not work correctly until all requirements are met.
```

**Root Cause**: Manifest declares compatibility with Claude Desktop 1.0.0+, but Claude Desktop is currently at version 0.14.x (pre-1.0 release).

**Status**: 🔧 **Known Issue - Fix In Progress**

This is a manifest versioning issue in the bundle. The team is updating the manifest to use the correct version range.

**Workaround**: Use manual installation instead:

<details>
<summary>Manual Installation for Claude Desktop (Click to expand)</summary>

1. **Open config file**:
   ```bash
   code ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. **Add server configuration**:
   ```json
   {
     "mcpServers": {
       "creative-juices": {
         "url": "https://ai.yuda.me/mcp/creative-juices/serve"
       }
     }
   }
   ```

3. **Restart Claude Desktop** (Cmd+Q then reopen)

4. **Verify**: Look for 🔨 icon in input area

</details>

**Expected Fix**: Manifest will be updated to require `>=0.7.0` instead of `>=1.0.0`, which matches actual Claude Desktop versions.

**Timeline**: Should be resolved in next deployment (check [GitHub releases](https://github.com/yudame/ai-skills/releases))

---

## Server Connection Issues

### Tools Not Appearing

**Check**:
1. Restart your MCP client after installation
2. Verify server URL is exactly: `https://ai.yuda.me/mcp/creative-juices/serve`
3. Check [server status](https://ai.yuda.me/mcp/creative-juices)

**Test server manually**:
```bash
curl -X POST https://ai.yuda.me/mcp/creative-juices/serve \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","params":{},"id":1}'
```

Should return JSON with 3 tools.

### Getting 404 Errors

**Symptom**: Server returns 404 Not Found

**Check**:
- URL must be `/serve` not just `/creative-juices`
- Correct: `https://ai.yuda.me/mcp/creative-juices/serve`
- Incorrect: `https://ai.yuda.me/mcp/creative-juices`

### Slow Response Times

**First call is slower**: Server might be cold-starting (~2-3 seconds)

**All calls are slow**: Check your network connection or corporate firewall

**Report persistent issues**: [GitHub Issues](https://github.com/yudame/ai-skills/issues)

---

## MCPB Bundle Technical Details

### Inspecting Bundle Contents

MCPB files are zip archives. To inspect:

```bash
# Download bundle
curl -O https://ai.yuda.me/mcp/creative-juices/download.mcpb

# Extract contents
unzip creative-juices.mcpb

# View manifest
cat manifest.json

# View proxy code
cat client.js
```

### Verify Bundle Works

After installation, check Claude Desktop logs:

**macOS**:
```bash
tail -f ~/Library/Logs/Claude/mcp*.log
```

Look for:
- ✅ `[creative-juices] Starting MCP server...`
- ✅ `[creative-juices] Connected to https://ai.yuda.me...`
- ❌ `Error: ...` (indicates problem)

---

## Platform-Specific Issues

### macOS

**Issue**: Bundle won't install
- **Check**: Node.js is available: `which node`
- **Fix**: Update Claude Desktop to latest version

**Issue**: "Extension damaged and can't be opened"
- **Check**: Download again (file may be corrupted)
- **Fix**: Clear downloads and re-download

### Windows

**Issue**: Config file location unclear
- **Location**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Access**: Press Win+R, paste path above

### Linux

**Issue**: Node.js version too old
- **Check**: `node --version` (need >=16.0.0)
- **Fix**: Update Node.js via system package manager

---

## Reporting Issues

When reporting issues, include:

1. **Platform**: macOS 14.x / Windows 11 / Ubuntu 22.04
2. **Claude Desktop Version**: Settings → About (e.g., 0.14.2)
3. **Node.js Version**: `node --version`
4. **Installation Method**: MCPB bundle / Manual config / Direct HTTP
5. **Error Message**: Copy full error text
6. **Logs**: Include relevant log excerpts (redact sensitive info)

**Report at**: https://github.com/yudame/ai-skills/issues

---

## Known Limitations

### Not Issues (Expected Behavior)

**Random Results**: Tools intentionally return different results each time. This is the point - embrace the chaos!

**No Context Awareness**: Tools don't know what you're working on. They just return random prompts for your AI to interpret.

**English Only**: Words and frameworks are currently English-only. Future versions may add other languages.

**Network Required**: MCPB bundles connect to hosted server. Offline mode not currently supported.

---

## Getting Help

- **Documentation**: https://github.com/yudame/ai-skills
- **Issues**: https://github.com/yudame/ai-skills/issues
- **Status**: https://ai.yuda.me
- **Tests**: Run `pytest tests/test_creative_juices.py -v` to verify server health

---

**Last Updated**: 2025-10-29
