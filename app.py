import asyncio
import sys
import os
import streamlit as st
from textwrap import dedent
from dotenv import load_dotenv
load_dotenv()


from agno.agent import Agent
from agno.tools.mcp import MCPTools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from agno.models.google import Gemini



st.set_page_config(page_title="Github MCP Agent", layout="wide")

st.markdown("<h1 class='main-header'> Github MCP Agent</h1>", unsafe_allow_html=True)
st.markdown("Explore GitHub repositories with natural language using the Model Context Protocol")



def run_async(coro):
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    finally:
        loop.close()


with st.sidebar:
    st.header("Authentication")
    github_token = st.text_input(
        "GitHub Token",
        type="password",
        help="Create a token with repo scope at github.com/settings/tokens"
    )

    if github_token:
        os.environ["GITHUB_TOKEN"] = github_token

    st.markdown("---")
    st.markdown("### Example Queries")

    st.markdown("**Issues**")
    st.markdown("- Show me issues by label")
    st.markdown("- What issues are being actively discussed?")

    st.markdown("**Pull Requests**")
    st.markdown("- What PRs need review?")
    st.markdown("- Show me recent merged PRs")

    st.markdown("**Repository**")
    st.markdown("- Show repository health metrics")
    st.markdown("- Show repository activity patterns")

    st.markdown("---")
    st.caption("Always specify the repository if not already included in your query.")



col1, col2 = st.columns([3, 1])

with col1:
    repo = st.text_input(
        "Repository",
        value="",  
        placeholder="owner/repo",
        help="Format: owner/repo"
    )

with col2:
    query_type = st.selectbox(
        "Query Type",
        ["Issues", "Pull Requests", "Repository Activity", "Custom"]
    )

query_template = ""
if query_type == "Issues":
    query_template = f"Find issues labeled as bugs in {repo}"
elif query_type == "Pull Requests":
    query_template = f"Show pull requests that need review in {repo}"
elif query_type == "Repository Activity":
    query_template = f"Show recent activity trends in {repo}"

query = st.text_area(
    "Your Query",
    value=query_template,
    placeholder="What would you like to know about this repository?"
)



model = Gemini(
    id="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

async def run_github_agent(message: str) -> str:
    if not os.getenv("GITHUB_TOKEN"):
        return "❌ Error: GitHub token not provided"
    
    if sys.platform == "win32":
        command = "cmd.exe"
        args = ["/c", "npx", "-y", "@modelcontextprotocol/server-github"]
    else:
        command = "npx"
        args = ["-y", "@modelcontextprotocol/server-github"]

    try:
        server_params = StdioServerParameters(
            command=command,
            args=args
        )

        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                mcp_tools = MCPTools(session=session)
                await mcp_tools.initialize()

                agent = Agent(
                    model=model,
                    tools=[mcp_tools],
                    instructions=dedent("""\
                        You are a GitHub assistant. Help users explore repositories and their activity.

                        - Provide organized, concise insights
                        - Focus on facts from the GitHub API
                        - Use Markdown formatting
                        - Present numerical data in tables
                        - Include links to relevant GitHub pages
                    """),
                    markdown=True
                )

                response = await agent.arun(message)
                return response.content

    except Exception:
        import traceback
        return f"❌ Internal Error:\n\n```\n{traceback.format_exc()}\n```"



if st.button("Run Query", type="primary", use_container_width=True):

    if not github_token:
        st.error("Please enter your GitHub token in the sidebar")

    elif not query.strip():
        st.error("Please enter a query")

    else:
        with st.spinner("Analyzing GitHub repository..."):
            if repo and repo not in query:
                full_query = f"{query} in {repo}"
            else:
                full_query = query

            result = run_async(run_github_agent(full_query))

        st.markdown("### Results")
        st.markdown(result)



if "result" not in st.session_state:
    st.markdown(
        """
        <div class='info-box'>
        <h4>How to use this app:</h4>
        <ol>
            <li>Enter your GitHub token</li>
            <li>Specify a repository</li>
            <li>Select a query type or write your own</li>
            <li>Click <b>Run Query</b></li>
        </ol>
        <p><b>Notes:</b></p>
        <ul>
            <li>MCP provides real-time GitHub access</li>
            <li>Be specific for better answers</li>
            <li>Node.js is required (for npx)</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.write("Built with Streamlit, Agno, and Model Context Protocol ")
