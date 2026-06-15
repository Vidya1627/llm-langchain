from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

chat_history = []

message = []
message.append(SystemMessage("respond in short paragraph"))

while True:
    query = input("You: ")
    if(query.lower() == "exit"):
        break
    
    chat_history.append(query)
    message.append(HumanMessage(query))

    result = model.invoke(message)

    print("AI: {}".format(result.content))
    
    chat_history.append(result.content)
    message.append(result)  # result type is AIMessage

print("----end of the conversation----")
print("Here is the complete chat history:")
print(chat_history)
