from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
load_dotenv()


messages = [
    SystemMessage(content = "Solve the following maths problem"),
    HumanMessage(content = "what is the square root of 49"),
]

# --------Google chat model

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result = llm.invoke(messages)
print(f"Answer from model is : {result.content}")

