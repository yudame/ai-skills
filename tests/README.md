# MCP Server Tests

Automated test suite for validating production MCP servers hosted at ai.yuda.me.

## Purpose

These tests serve as:
1. **Live Documentation** - Proves the servers work as documented
2. **Health Monitoring** - Continuous validation via GitHub Actions
3. **API Contract** - Documents expected behavior and responses
4. **Public Trust** - Open source tests anyone can run

## Running Tests Locally

### Setup

```bash
# Install dependencies
pip install -r tests/requirements.txt

# Or with uv (recommended)
uv pip install -r tests/requirements.txt
```

### Run All Tests

```bash
# Run with verbose output
pytest tests/test_creative_juices.py -v

# Run specific test class
pytest tests/test_creative_juices.py::TestGetInspiration -v

# Run specific test
pytest tests/test_creative_juices.py::TestGetInspiration::test_tool_returns_sparks -v
```

### Run with Coverage

```bash
pytest tests/ --cov --cov-report=html
open htmlcov/index.html
```

## Test Structure

### TestServerHealth
- Server reachability
- Basic HTTP response validation
- JSON content type verification

### TestMCPProtocol
- MCP protocol compliance
- Initialize handshake
- Tools listing
- Protocol version compatibility

### TestGetInspiration
- Returns 3 verb-noun combinations
- Sparks follow expected format
- Randomness verification
- Response structure validation

### TestThinkOutsideTheBox
- Returns intense combinations
- Instruction tone verification
- Response structure validation

### TestRealityCheck
- Returns 4 strategic questions
- Framework validation (first_principles, limit_thinking, platonic_ideal, optimization)
- Question format validation

### TestPerformance
- Response time benchmarks
- Concurrent request handling
- Load testing

### TestErrorHandling
- Invalid tool names
- Malformed requests
- Graceful error responses

## Continuous Integration

Tests run automatically on:
- **Every push** to main branch
- **Every pull request**
- **Scheduled**: Every 6 hours (monitors production health)

See `.github/workflows/test-mcp-servers.yml` for CI configuration.

## Status Badges

Production server status badges are displayed in the main README.

## Expected Failures

Some tests may fail if:
- Server is temporarily down for maintenance
- Network connectivity issues
- API changes (intentional breaking changes)

Check https://ai.yuda.me for status updates during outages.

## Contributing

To add tests for new MCP servers:

1. Create `tests/test_{server_name}.py`
2. Follow the pattern from `test_creative_juices.py`
3. Update CI workflow to include new test file
4. Add status badge to main README

## Test Coverage Goals

- ✅ Health checks
- ✅ MCP protocol compliance
- ✅ All tool endpoints
- ✅ Response format validation
- ✅ Performance benchmarks
- ✅ Error handling
- 🔲 Rate limiting (if implemented)
- 🔲 Authentication (if implemented)

## Debugging Failed Tests

### Server Unreachable
```bash
# Test connectivity manually
curl -X POST https://ai.yuda.me/mcp/creative-juices/serve \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","params":{},"id":1}'
```

### Unexpected Response Format
```bash
# Capture full response for debugging
pytest tests/ -v -s --tb=long
```

### Performance Issues
```bash
# Run performance tests only
pytest tests/test_creative_juices.py::TestPerformance -v
```

## License

Tests are MIT licensed - use them for your own MCP servers!
