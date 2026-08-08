from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="openrouter/free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3
)

def ask_ai(prompt):
    response = llm.invoke(prompt)
    return response.content