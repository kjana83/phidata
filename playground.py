from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import phi
from phi.playground import Playground, serve_playground_app

import os
from dotenv import load_dotenv
load_dotenv()
phi.api =os.getenv("PHI_API_KEY") 


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

app = Playground( agents=[web_search_agent, financial_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
