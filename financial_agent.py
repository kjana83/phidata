from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
from dotenv import load_dotenv
load_dotenv()


## Web search agent
web_search_agent = Agent(
  name = "web_search_agent",
  roles = "Search web for information",
  model = Groq(id="llama-3.3-70b-versatile"),
  tools = [DuckDuckGo()],
  instructions = ["Always include sources for information"],
  show_tool_calls=True,
  markdown = True,
)

## Financial agent
financial_agent = Agent(
  name = "financial_agent",
  model = Groq(id="llama-3.3-70b-versatile"),
  roles = "Financial analysis",
  tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
  instructions = ["Use tables to display the data"],
  show_tool_calls=True,
  markdown = True,  
)

multi_ai_agent = Agent(
  model = Groq(id="llama-3.3-70b-versatile"),
  team=[web_search_agent, financial_agent],
  instructions=["Always include sources for information", "Use tables to display the data"],
  show_tool_calls=True,
  markdown=True,

)

multi_ai_agent.print_response("Summarize analyst recommendations for NVDA stock", stream=True)
