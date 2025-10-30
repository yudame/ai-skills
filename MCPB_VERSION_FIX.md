# MCPB Bundle Version Compatibility Fix

## Issue

MCPB bundles fail to install in Claude Desktop with version requirement error:

```
Requirements
an update to Claude Desktop
Claude Desktop >=1.0.0
```

**Problem**: Manifest declares compatibility with Claude Desktop `>=1.0.0`, but Claude Desktop is currently at version `0.14.x` (pre-1.0 release).

## Root Cause

File: `apps/ai/mcp/bundles/creative-juices/manifest.json` (and `cto-tools/manifest.json`)

```json
"compatibility": {
  "claude_desktop": ">=1.0.0",  // ❌ Version doesn't exist yet
```

## The Fix

### Files to Update

1. `apps/ai/mcp/bundles/creative-juices/manifest.json`
2. `apps/ai/mcp/bundles/cto-tools/manifest.json`

### Change Required

```diff
  "compatibility": {
-   "claude_desktop": ">=1.0.0",
+   "claude_desktop": ">=0.7.0",
    "platforms": [
      "darwin",
      "win32",
      "linux"
    ],
```

### Version Rationale

**Why `>=0.7.0`?**

- MCPB support was added in Claude Desktop ~0.7.x
- Current stable version: 0.14.x
- Allows all modern Claude Desktop versions
- Future-proof for 1.0.0 when it releases

**Alternative versions**:
- `>=0.10.0` - More conservative, still covers most users
- `>=0.7.0` - Maximum compatibility
- `>=0.14.0` - Latest only (too restrictive)

**Recommendation**: Use `>=0.7.0` for broadest compatibility.

## Testing After Fix

### 1. Rebuild Bundles

```bash
cd apps/ai/mcp/bundles
./build.sh creative-juices
./build.sh cto-tools
```

### 2. Verify Manifest

```bash
unzip -p creative-juices.mcpb manifest.json | grep claude_desktop
# Should show: "claude_desktop": ">=0.7.0"
```

### 3. Test Installation

1. Download updated bundle from https://ai.yuda.me/mcp/creative-juices/download.mcpb
2. Install in Claude Desktop (Settings → Extensions → Install from file)
3. Should install without version warning
4. Restart Claude Desktop
5. Verify tools appear (🔨 icon)

## Impact

**Before Fix**:
- ❌ Users see version requirement error
- ❌ Must use manual config workaround
- ❌ Poor user experience

**After Fix**:
- ✅ One-click installation works
- ✅ No version warnings
- ✅ Smooth user experience

## Deploy

1. Update both manifest.json files in cuttlefish repo
2. Rebuild bundles: `./build.sh creative-juices && ./build.sh cto-tools`
3. Deploy to Render (auto-deploys from main branch)
4. Verify downloads serve updated bundles
5. Test installation in Claude Desktop 0.14.x

## Workaround (Until Fixed)

Users experiencing this issue should use manual installation:

**Claude Desktop - Manual Config**:
```json
{
  "mcpServers": {
    "creative-juices": {
      "url": "https://ai.yuda.me/mcp/creative-juices/serve"
    }
  }
}
```

Config location: `~/Library/Application Support/Claude/claude_desktop_config.json`

See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for detailed workaround instructions.

---

**Priority**: HIGH - Blocks one-click installation feature
**Effort**: LOW - Simple version string change
**Files**: 2 manifests + rebuild bundles
**Testing**: Quick - just verify install in Claude Desktop

---

**Created**: 2025-10-29
**Status**: Documented, awaiting fix in cuttlefish repo
