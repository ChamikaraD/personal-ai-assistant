from langgraph.constants import END
from langgraph.graph import StateGraph
from typing_extensions import TypedDict

from agents import router_agent, news_agent, scam_agent, general_agent, writing_agent
from guardrails import input_guardrails_node


class AgentState(TypedDict):
    input: str
    route: str
    response: str
    blocked: bool
    reason: str
    agent: str

def input_decision(state: AgentState):
    if state.get("blocked"):
        return "end"
    return "router"

def router_decision(state: AgentState):
    return state["route"]   # news, scam, general ,write

graph = StateGraph(AgentState)


graph.add_node("input_guard", input_guardrails_node)
graph.add_node("router", router_agent)
graph.add_node("news_agent", news_agent)
graph.add_node("scam_agent", scam_agent)
graph.add_node("general_agent", general_agent)
graph.add_node("writing_agent", writing_agent)


graph.set_entry_point("input_guard")

graph.add_conditional_edges(
    "input_guard",
    input_decision,
    {
        "router": "router",
        "end": END
    }
)


graph.add_conditional_edges(
    "router",
    router_decision,
    {
        "news": "news_agent",
        "scam": "scam_agent",
        "general": "general_agent" ,
        "writing" : "writing_agent"
    }
)

graph.add_edge("news_agent", END)
graph.add_edge("scam_agent", END)
graph.add_edge("scam_agent", END)
graph.add_edge("writing_agent", END)


compiled_graph = graph.compile()
