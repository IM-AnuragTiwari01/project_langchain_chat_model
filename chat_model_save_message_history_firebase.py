from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
#from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_firestore import FirestoreChatMessageHistory
from google.cloud import firestore

load_dotenv()

#set up fire base firestore

PROJECT_ID = "langchain-524f7"
SESSION_ID = "user_session_new"
COLLECTION_NAME = "chat_history"

#Inititalize Firestore Client
print("Initiallizing Firestore Client...")
client = firestore.Client(project = PROJECT_ID)


# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# Initialize Chat Model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")


print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")