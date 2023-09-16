import os
from environs import Env
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


# Read our .env file
env = Env()
env.read_env()

# Define a dictionary of expected environment variables
env_vars = {
    "OPEN_AI_SECRET_KEY": None,
    "NEO4J_URI": None,
    "NEO4J_USERNAME": None,
    "NEO4J_PASSWORD": None,
    "AURA_INSTANCEID": None,
    "AURA_INSTANCENAME": None,
}

# Load environment variables from .env into the dictionary
for key in env_vars:
    env_vars[key] = os.environ.get(key)

# Neo4j Aura credentials
url = os.environ.get("NEO4J_URI")
username = os.environ.get("NEO4J_USERNAME")
password = os.environ.get("NEO4J_PASSWORD")

# OpenAI credentials
openai_api_secret_key = os.environ.get("OPEN_AI_SECRET_KEY")

# Instantiate Neo4j vector from an existing vector
# CYPHER - "SHOW INDEXES;" will show we have an index type Vector named "vector"
index_name = "vector"  # default index name
neo4j_vector = Neo4jVector.from_existing_index(
    OpenAIEmbeddings(openai_api_key=openai_api_secret_key),
    url=url,
    username=username,
    password=password,
    index_name=index_name,
)

# Question-Answer Workflow With LangChain
try:
    chain = RetrievalQAWithSourcesChain.from_chain_type(
        ChatOpenAI(temperature=0, openai_api_key=openai_api_secret_key),
        chain_type="stuff",
        retriever=neo4j_vector.as_retriever(),
    )

    query = "What is Euler credited for popularizing?"

    chain(
        {"question": query},
        return_only_outputs=True,
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(temperature=0, openai_api_key=openai_api_secret_key),
        neo4j_vector.as_retriever(),
        memory=memory,
    )

    print(qa({"question": query})["answer"])

except Exception as e:
    print(f"An unexpected error occurred: {e}")
