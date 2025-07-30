from agnoagent.agent import Agent
from agnoagent.models.openai import GeminiOpenAI as OpenAIChat
from agnoagent.tools.yfinance import YFinance as YFinanceTools

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from agnoagent.builder import AgentBuilder

from agnoagent.models.openai import GeminiOpenAI
from agnoagent.tools.yfinance import YFinanceTool


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Create your agent (using finance tool)
agent = Agent(
    model=OpenAIChat(id="gpt‑4o"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Quickly answer queries, fetch stock price when asked",
    markdown=False
)

# In-memory chat history
chat_history = []

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "history": chat_history})

@app.post("/chat")
async def chat_endpoint(msg: Message):
    user_message = msg.message.strip()
    if not user_message:
        return JSONResponse(content={"response": "⚠️ Please enter a valid message."})

    chat_history.append({"sender": "user", "text": user_message})

    try:
        response_text = agent.chat(user_message)
        chat_history.append({"sender": "bot", "text": response_text})
        return JSONResponse(content={"response": response_text})
    except Exception as e:
        err = f"⚠️ Internal Error: {e}"
        chat_history.append({"sender": "bot", "text": err})
        return JSONResponse(content={"response": err})
