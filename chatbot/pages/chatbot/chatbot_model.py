from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

from environment.settings import APP_OPENAI_API_KEY

chat = OpenAI(openai_api_key=APP_OPENAI_API_KEY,temperature=0)

conversation = ConversationChain(
    llm=chat, 
    verbose=True,
    memory=ConversationBufferMemory()
)
