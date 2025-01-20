from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def suomenna():
    return "Perkele!"

if __name__ == "__main__":
    mcp.run(transport='stdio')