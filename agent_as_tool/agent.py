from google.adk.agents import Agent
from google.adk.tools import google_search, AgentTool


def convert_temperature(value: float, unit: str) -> dict:
    """Convert temperature between Celsius and Fahrenheit."""
    unit = unit.upper()
    if unit == "C":
        converted = (value * 9/5) + 32
        return {"status": "success", "report": f"{value}°C is {converted:.2f}°F"}
    elif unit == "F":
        converted = (value - 32) * 5/9
        return {"status": "success", "report": f"{value}°F is {converted:.2f}°C"}
    else:
        return {
            "status": "error",
            "error_message": f"Unknown unit {unit}. Please use 'C' or 'F'."
        }

search_agent = Agent(
    model='gemini-2.0-flash-001',
    name='search_agent',
    tools=[google_search],
    description='An assistant that helps with queries and searches the internet.',
    instruction='''
        You are a helpful Search assistant.
        When the user asks about current events or factual information, use the google_search tool.
        Always return a clear, short explanation.
    '''
)

search_agent_tool = AgentTool(search_agent)

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    tools=[convert_temperature, search_agent_tool],
    description='An assistant that helps with temperature conversion and factual queries.',
    instruction='''
        You are a helpful assistant.
        Use the convert_temperature tool for temperature conversion questions.
        Use the search tool for factual queries.
        Always return a clear, short explanation.
    '''
)