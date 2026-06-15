from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

message = [
    SystemMessage("give answers in bullet points"),
    HumanMessage("summerise the book Mahasamar"),
]

result = model.invoke(message)

print(result)