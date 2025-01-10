from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate

from langchain_community.tools.tavily_search import TavilySearchResults

def hello(input):
    return input

def create_openai_agent(model):
    tools = [Tool(name="Test", func=hello, description="tool placeholder saying hello")]

    llm = ChatOpenAI(temperature=.33, model=model)

    agent = initialize_agent(tools, llm)

    return agent