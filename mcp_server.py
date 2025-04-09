from typing import Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("eclipse")

@mcp.tool()
async def multiplication(a: int, b: int) -> int:
    return a * b

@mcp.tool()
async def addition(a: int, b: int) -> int:
    return a + b


@mcp.tool()
async def subtraction(a: int, b: int) -> int:
    return a - b

@mcp.tool()
async def division(a: int, b: int) -> int:
    return a / b


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')