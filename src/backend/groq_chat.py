from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain

from src.config.constants import Roles
from src.config.env import settings


chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", api_key=settings.APP.GROQ_API_KEY)

def req_groq_langchain(role, msg):
    system = f"{role}\n\nYou must respond concisely, directly, and without unnecessary fillers or pleasantries."
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    memory = ConversationBufferWindowMemory(k=2, memory_key="chat_history")

    chain = LLMChain(llm=chat, prompt=prompt, memory=memory)

    output = chain.invoke({"text": f"{msg}"})
    print(output)
    return output["text"]
    
if __name__ == "__main__":
    req_groq_langchain(Roles.IDEATION_ROADMAP, "I am starting a facebook clone called netbox")
