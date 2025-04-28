from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage, AIMessage
load_dotenv()


# messages = [
#     SystemMessage(content = "Solve the following maths problem"),
#     HumanMessage(content = "what is the square root of 49"),
# ]


# --------Google chat model

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

chat_history = [] # use this to store prev messages

system_message = SystemMessage(content = "You are a helpful ai assistant")

chat_history.append(system_message) #added the system_message to the history


#chat loop
#chat can be exited by typing exit and enter

while True:
    query = input("You: ")
    if query.lower()=="exit":
        break # exit the conversation
    chat_history.append(HumanMessage(content = query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content = response))

    print(f"AI response: {response}")

print("-------Message History------------")
print(chat_history)














