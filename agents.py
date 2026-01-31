from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from system_prompts import ROUTER_AGENT_SYSTEM_PROMPT, NEWS_AGENT_PROMPT, SCAM_PROMPT, GENERAL_AGENT_PROMPT, \
    WRITING_AGENT_PROMPT

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini-2025-04-14")


def router_agent(state):
    prompt = ChatPromptTemplate.from_messages([
        ("system", ROUTER_AGENT_SYSTEM_PROMPT),
        ("human", "{input}")
    ])

    routing_chain = prompt | llm
    agent_category = routing_chain.invoke({"input": state["input"]})


    return {
        "route": agent_category.content.strip().lower()
    }

def scam_agent(state):
    prompt = ChatPromptTemplate.from_messages([
        ("system", SCAM_PROMPT),
        ("human", "{input}")
    ])

    scam_chain = prompt | llm
    scam_response  = scam_chain.invoke({"input": state["input"]})

    return {"response" : scam_response}



def news_agent(state):
    search_tool = TavilySearch(max_results=5)

    agent = create_agent(
        model=llm,
        system_prompt=NEWS_AGENT_PROMPT,
        tools=[search_tool]
    )

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": state["input"]}
        ]
    })

    return {
        "response": result["messages"][-1].content,
        "agent": "news"
    }

def general_agent(state):
    """
        Handles general informational and explanatory questions.
        """
    prompt = ChatPromptTemplate.from_messages([
        ("system", GENERAL_AGENT_PROMPT),
        ("human", "{input}")
    ])

    chain = prompt | llm
    result = chain.invoke({"input": state["input"]})

    return {
        "response": result.content,
        "agent": "General Agent"
    }

def writing_agent(state):
    """
        Handles writing, rewriting, and text improvement tasks.
        """
    prompt = ChatPromptTemplate.from_messages([
        ("system", WRITING_AGENT_PROMPT),
        ("human", "{input}")
    ])

    chain = prompt | llm
    result = chain.invoke({"input": state["input"]})

    return {
        "response": result.content,
        "agent":"Writing Agent"
    }




    result = agent.invoke({
        "messages" : [
            {
                "role" : "user" ,
                "content" : state["input"]
            }
        ]
    }
    )

    return {"response" : result["messages"][-1].content}