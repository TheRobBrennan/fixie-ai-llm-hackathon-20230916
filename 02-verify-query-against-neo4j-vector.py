import os
from environs import Env
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings.openai import OpenAIEmbeddings

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

# Vector Similarity Search
try:
    # VERIFY: Simple vector similarity search to verify that everything works as intended.
    query = "Where did Euler grow up?"

    # The LangChain module used the specified embedding function (OpenAI in this example) to embed the question and then find the most similar documents by comparing the cosine similarity between the user question and indexed documents.
    # Neo4j Vector index also supports the Euclidean similarity metric along with the cosine similarity.
    results = neo4j_vector.similarity_search(query)
    print(results[0].page_content)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
