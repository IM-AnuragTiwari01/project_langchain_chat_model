from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max"

prompt_template = ChatPromptTemplate.from_template(template)

prompt =  prompt_template.invoke({
    "tone": "energetic", 
    "company": "samsung", 
    "position": "AI Engineer", 
    "skill": "AI"
})

# Example 2: Prompt with System and Human Messages (Using Tuples)
# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}."),
#     ("human", "Tell me {joke_count} jokes."),
# ]

# prompt_template = ChatPromptTemplate.from_messages(messages)  #when using tuples as prompt template
# prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})

result = llm.invoke(prompt)
print(result.content)
