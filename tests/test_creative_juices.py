#!/usr/bin/env python3
"""
Test suite for Creative Juices MCP Server
Tests against production endpoint: https://ai.yuda.me/mcp/creative-juices/serve

Run with: pytest tests/test_creative_juices.py -v
"""

import json
import pytest
import requests
from typing import Dict, List, Any

# Production server endpoint
SERVER_URL = "https://ai.yuda.me/mcp/creative-juices/serve"
TIMEOUT = 10  # seconds


class TestServerHealth:
    """Test basic server availability and health"""

    def test_server_is_reachable(self):
        """Verify server responds to HTTP requests"""
        response = requests.get(SERVER_URL, timeout=TIMEOUT)
        assert response.status_code in [200, 405], \
            f"Server returned unexpected status: {response.status_code}"

    def test_server_returns_json(self):
        """Verify server returns JSON content type"""
        response = requests.post(
            SERVER_URL,
            json={"jsonrpc": "2.0", "method": "initialize", "params": {}, "id": 1},
            timeout=TIMEOUT
        )
        assert "application/json" in response.headers.get("Content-Type", ""), \
            "Server should return JSON content type"


class TestMCPProtocol:
    """Test MCP protocol compliance"""

    def test_jsonrpc_initialize(self):
        """Test MCP initialize handshake"""
        payload = {
            "jsonrpc": "2.0",
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            },
            "id": 1
        }

        response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)
        assert response.status_code == 200, f"Initialize failed with status {response.status_code}"

        data = response.json()
        assert "result" in data, "Initialize response missing 'result'"
        assert "capabilities" in data["result"], "Response missing capabilities"
        assert "serverInfo" in data["result"], "Response missing serverInfo"

    def test_tools_list(self):
        """Test tools/list endpoint returns expected tools"""
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/list",
            "params": {},
            "id": 2
        }

        response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)
        assert response.status_code == 200, f"tools/list failed with status {response.status_code}"

        data = response.json()
        assert "result" in data, "Response missing 'result'"
        assert "tools" in data["result"], "Response missing 'tools' array"

        tools = data["result"]["tools"]
        tool_names = [tool["name"] for tool in tools]

        # Verify all three expected tools are present
        assert "get_inspiration" in tool_names, "Missing get_inspiration tool"
        assert "think_outside_the_box" in tool_names, "Missing think_outside_the_box tool"
        assert "reality_check" in tool_names, "Missing reality_check tool"

        return tools  # Return for inspection


class TestGetInspiration:
    """Test get_inspiration tool"""

    def test_tool_returns_sparks(self):
        """Verify get_inspiration returns 3 verb-noun combinations"""
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "get_inspiration",
                "arguments": {}
            },
            "id": 3
        }

        response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)
        assert response.status_code == 200, f"Tool call failed with status {response.status_code}"

        data = response.json()
        assert "result" in data, "Response missing 'result'"

        result = data["result"]
        assert "content" in result, "Result missing 'content'"

        # Parse the content
        content = result["content"]
        assert isinstance(content, list), "Content should be an array"
        assert len(content) > 0, "Content array is empty"

        # Get the text content
        text_content = content[0]["text"] if isinstance(content[0], dict) else content[0]
        result_data = json.loads(text_content)

        assert "sparks" in result_data, "Response missing 'sparks'"
        assert "instruction" in result_data, "Response missing 'instruction'"

        sparks = result_data["sparks"]
        assert isinstance(sparks, list), "Sparks should be an array"
        assert len(sparks) == 3, f"Expected 3 sparks, got {len(sparks)}"

        # Verify each spark is a verb-noun combination
        for spark in sparks:
            assert isinstance(spark, str), f"Spark should be string, got {type(spark)}"
            assert "-" in spark, f"Spark should contain hyphen: {spark}"
            parts = spark.split("-")
            assert len(parts) == 2, f"Spark should be verb-noun pair: {spark}"

    def test_sparks_are_random(self):
        """Verify multiple calls return different sparks (probabilistic)"""
        results = []

        for _ in range(3):
            payload = {
                "jsonrpc": "2.0",
                "method": "tools/call",
                "params": {
                    "name": "get_inspiration",
                    "arguments": {}
                },
                "id": 4
            }

            response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)
            data = response.json()
            content = data["result"]["content"]
            text_content = content[0]["text"] if isinstance(content[0], dict) else content[0]
            result_data = json.loads(text_content)
            results.append(tuple(result_data["sparks"]))

        # At least one result should be different (very high probability with 600+ words)
        unique_results = set(results)
        assert len(unique_results) > 1, "All calls returned identical sparks - randomness might be broken"


class TestThinkOutsideTheBox:
    """Test think_outside_the_box tool"""

    def test_tool_returns_intense_sparks(self):
        """Verify think_outside_the_box returns 3 intense combinations"""
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "think_outside_the_box",
                "arguments": {}
            },
            "id": 5
        }

        response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)
        assert response.status_code == 200, f"Tool call failed with status {response.status_code}"

        data = response.json()
        result = data["result"]
        content = result["content"]
        text_content = content[0]["text"] if isinstance(content[0], dict) else content[0]
        result_data = json.loads(text_content)

        assert "sparks" in result_data, "Response missing 'sparks'"
        assert "instruction" in result_data, "Response missing 'instruction'"

        sparks = result_data["sparks"]
        assert len(sparks) == 3, f"Expected 3 sparks, got {len(sparks)}"

        # Verify instruction mentions intensity
        instruction = result_data["instruction"]
        assert any(word in instruction.lower() for word in ["shatter", "intense", "radical"]), \
            "Instruction should convey intensity"


class TestRealityCheck:
    """Test reality_check tool"""

    def test_tool_returns_strategic_questions(self):
        """Verify reality_check returns 4 strategic questions from frameworks"""
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "reality_check",
                "arguments": {}
            },
            "id": 6
        }

        response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)
        assert response.status_code == 200, f"Tool call failed with status {response.status_code}"

        data = response.json()
        result = data["result"]
        content = result["content"]
        text_content = content[0]["text"] if isinstance(content[0], dict) else content[0]
        result_data = json.loads(text_content)

        assert "questions" in result_data, "Response missing 'questions'"
        assert "frameworks" in result_data, "Response missing 'frameworks'"
        assert "instruction" in result_data, "Response missing 'instruction'"

        questions = result_data["questions"]
        frameworks = result_data["frameworks"]

        assert len(questions) == 4, f"Expected 4 questions, got {len(questions)}"
        assert len(frameworks) == 4, f"Expected 4 frameworks, got {len(frameworks)}"

        # Verify expected frameworks are present
        expected_frameworks = ["first_principles", "limit_thinking", "platonic_ideal", "optimization"]
        for framework in expected_frameworks:
            assert framework in frameworks, f"Missing framework: {framework}"

        # Verify questions are non-empty strings
        for question in questions:
            assert isinstance(question, str), "Question should be string"
            assert len(question) > 10, "Question seems too short"
            assert "?" in question, "Question should end with question mark"


class TestPerformance:
    """Test server performance characteristics"""

    def test_response_time(self):
        """Verify server responds within acceptable time"""
        import time

        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "get_inspiration",
                "arguments": {}
            },
            "id": 7
        }

        start = time.time()
        response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)
        elapsed = time.time() - start

        assert response.status_code == 200, "Request failed"
        assert elapsed < 5.0, f"Response took {elapsed:.2f}s (threshold: 5s)"

    def test_concurrent_requests(self):
        """Verify server handles multiple concurrent requests"""
        import concurrent.futures

        def make_request():
            payload = {
                "jsonrpc": "2.0",
                "method": "tools/call",
                "params": {
                    "name": "get_inspiration",
                    "arguments": {}
                },
                "id": 8
            }
            response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)
            return response.status_code

        # Make 5 concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(make_request) for _ in range(5)]
            results = [f.result() for f in concurrent.futures.as_completed(futures)]

        # All should succeed
        assert all(status == 200 for status in results), "Some concurrent requests failed"


class TestErrorHandling:
    """Test server error handling"""

    def test_invalid_tool_name(self):
        """Verify server handles invalid tool names gracefully"""
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "nonexistent_tool",
                "arguments": {}
            },
            "id": 9
        }

        response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)
        data = response.json()

        # Should return error in JSON-RPC format
        assert "error" in data, "Should return error for invalid tool"

    def test_malformed_request(self):
        """Verify server handles malformed JSON-RPC requests"""
        payload = {
            "not_jsonrpc": "invalid"
        }

        response = requests.post(SERVER_URL, json=payload, timeout=TIMEOUT)

        # Should handle gracefully (either error response or 400 status)
        assert response.status_code in [200, 400], "Should handle malformed request gracefully"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
