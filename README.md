# DuckDuckGo MCP Server

A Model Context Protocol (MCP) server that provides DuckDuckGo search capabilities to AI assistants and other MCP clients.

[![smithery badge](https://smithery.ai/badge/@tdu-naifen/duckduckgomcp)](https://smithery.ai/server/@tdu-naifen/duckduckgomcp)

## Features

- **Web Search**: Search DuckDuckGo for web results with titles, URLs, and snippets
- **Configurable Results**: Control the number of results returned (1-20)
- **Region Support**: Search with specific regional preferences
- **Fast & Reliable**: Built with the FastMCP framework for optimal performance

## Installation

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/tdu-naifen/DuckDuckGoMCP.git
   cd DuckDuckGoMCP
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Install the package:
   ```bash
   uv pip install -e .
   ```

## Usage

### Running the Server

Start the MCP server:
```bash
uv run duckduckgo-mcp
```

The server will start and listen for MCP client connections via stdio.

### Available Tools

#### `duckduckgo_search`

Search DuckDuckGo and return formatted results.

**Parameters:**
- `query` (string, required): The search query to execute
- `max_results` (integer, optional): Maximum number of results (default: 10, max: 20)
- `region` (string, optional): Region code for localized results (default: "wt-wt")

**Example:**
```json
{
  "tool": "duckduckgo_search",
  "arguments": {
    "query": "python programming tutorials",
    "max_results": 5,
    "region": "us-en"
  }
}
```

### Region Codes

Common region codes include:
- `us-en`: United States (English)
- `uk-en`: United Kingdom (English)
- `de-de`: Germany (German)
- `fr-fr`: France (French)
- `wt-wt`: Global (default)

## Testing

Run the test suite to verify functionality:

```bash
# Test the search function directly
uv run python test_server.py

# Test the full MCP protocol
uv run python test_mcp_client.py
```

## Configuration with MCP Clients

### Claude Desktop

Add this to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "duckduckgo-search": {
      "command": "uv",
      "args": ["run", "duckduckgo-mcp"],
      "cwd": "/path/to/DuckDuckGoMCP"
    }
  }
}
```

### Other MCP Clients

For other MCP clients, use the command:
```bash
uv run duckduckgo-mcp
```

## Development

### Project Structure

```
DuckDuckGoMCP/
├── duckduckgo_mcp/
│   ├── __init__.py
│   └── server.py          # Main server implementation
├── test_server.py         # Direct function tests
├── test_mcp_client.py     # MCP protocol tests
├── pyproject.toml         # Project configuration
├── smithery.yaml          # Smithery configuration
└── README.md
```

### Dependencies

- `mcp>=1.0.0`: Model Context Protocol framework
- `duckduckgo-search>=6.0.0`: DuckDuckGo search API client

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure functionality
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Author

**Tingzhen Du**

## Notes

- The DuckDuckGo Search library may show deprecation warnings about renaming to `ddgs`. This is a known issue and doesn't affect functionality.
- Search results are returned with moderate SafeSearch filtering enabled.
- The server respects DuckDuckGo's rate limiting and terms of service.
