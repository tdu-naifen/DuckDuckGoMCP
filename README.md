# DuckDuckGo MCP Server

A **Model Context Protocol (MCP)** server that provides DuckDuckGo search capabilities. Built with UV for fast dependency management.

## Features

- **🔍 DuckDuckGo Search**: Search the web using DuckDuckGo's API with the `duckduckgo-search` library
- **🚀 UV Optimized**: Built with UV for fast dependency management
- **� Simple Integration**: Easy setup for Claude Desktop and other MCP clients

## Tool Provided

### `duckduckgo_search`
Search DuckDuckGo and return formatted results with titles, URLs, and snippets.

**Parameters:**
- `query` (required): The search query string
- `max_results` (optional): Maximum number of results (1-20, default: 10)
- `region` (optional): Search region (default: "wt-wt" for worldwide)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd DuckDuckGoMCP

# Install dependencies with UV
uv sync

# Run the server
uv run duckduckgo-mcp
```

## Configuration for Claude Desktop

Add this to your Claude Desktop configuration file:

**Location:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

**Configuration:**
```json
{
  "mcpServers": {
    "duckduckgo": {
      "command": "uv",
      "args": [
        "run",
        "duckduckgo-mcp"
      ],
      "cwd": "/path/to/DuckDuckGoMCP"
    }
  }
}
```

## Project Structure

```
DuckDuckGoMCP/
├── duckduckgo_mcp/
│   ├── __init__.py
│   └── server.py          # Main MCP server implementation
├── pyproject.toml         # Project configuration (UV optimized)
└── README.md              # This file
```

## Usage

Once configured with Claude Desktop, you can use the search tool in your conversations:

**Example:** "Search DuckDuckGo for 'Python async programming best practices'"

## License

MIT License
