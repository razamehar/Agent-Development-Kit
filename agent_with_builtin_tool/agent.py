from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model="gemini-2.0-flash-001",
    name="agent_with_builtin_tool",
    tools=[google_search],  # directly include the tool
    description="An assistant that can answer questions and search the internet when needed.",
    instruction="""
        You are a helpful assistant.
        When the user asks about current events or factual information, use the google_search tool.
        Always return a clear, short explanation.
    """
)
