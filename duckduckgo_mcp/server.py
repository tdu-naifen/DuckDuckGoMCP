#!/usr/bin/env python3
"""
DuckDuckGo MCP Server

A Model Context Protocol server that provides DuckDuckGo search capabilities.
"""

import logging

from duckduckgo_search import DDGS
from mcp.server import FastMCP

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("duckduckgo-mcp")

# Initialize the FastMCP server
mcp = FastMCP("duckduckgo-mcp")


@mcp.tool()
def duckduckgo_search(
    query: str,
    max_results: int = 10,
    region: str = "wt-wt"
) -> str:
    """
    Search DuckDuckGo and return a list of search results with titles, URLs, and snippets.
    
    Args:
        query: The search query to execute on DuckDuckGo
        max_results: Maximum number of results to return (default: 10, max: 20)
        region: Region for search results (e.g., 'us-en', 'uk-en', 'de-de', default: 'wt-wt')
    
    Returns:
        Formatted search results with titles, URLs, and snippets
    """
    if not query:
        raise ValueError("Query parameter is required")
    
    # Ensure max_results is within bounds
    max_results = max(1, min(20, max_results))
    
    logger.info(f"Searching DuckDuckGo for: '{query}' (max_results: {max_results}, region: {region})")
    
    try:
        # Use DDGS for search
        with DDGS() as ddgs:
            results = list(ddgs.text(
                keywords=query,
                region=region,
                safesearch="moderate",
                max_results=max_results
            ))
        
        if not results:
            return f"No search results found for query: '{query}'"
        
        # Format results
        formatted_results = []
        for i, result in enumerate(results, 1):
            formatted_result = f"**Result {i}:**\n"
            formatted_result += f"**Title:** {result.get('title', 'N/A')}\n"
            formatted_result += f"**URL:** {result.get('href', 'N/A')}\n"
            formatted_result += f"**Snippet:** {result.get('body', 'N/A')}\n"
            formatted_results.append(formatted_result)
        
        response_text = f"Found {len(results)} search results for query: '{query}'\n\n"
        response_text += "\n---\n\n".join(formatted_results)
        
        return response_text
    
    except Exception as e:
        logger.error(f"DuckDuckGo search error: {str(e)}")
        raise ValueError(f"Search failed: {str(e)}")


def main_sync() -> None:
    """Synchronous main entry point for the server."""
    mcp.run()


if __name__ == "__main__":
    main_sync()
