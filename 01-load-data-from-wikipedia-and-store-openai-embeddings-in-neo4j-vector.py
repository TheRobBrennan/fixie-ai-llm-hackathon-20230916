# Modularizing Wikipedia Data Loading and Processing
import os
from environment_utilities import (
    load_environment_variables,
    verify_environment_variables,
)

from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.document_loaders import WikipediaLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# Load environment variables using the utility
env_vars = load_environment_variables()

# Verify the environment variables
if not verify_environment_variables(env_vars):
    raise ValueError("Some environment variables are missing!")


def load_wikipedia_data(query: str):
    """
    Load data from Wikipedia based on the given query.
    This function is a mock since the actual module isn't available in this environment.
    """
    # Reading and chunking a Wikipedia article
    # https://neo4j.com/developer-blog/langchain-library-full-support-neo4j-vector-index/
    query = "Leonhard Euler"

    # Read the wikipedia article
    raw_documents = WikipediaLoader(query=query).load()

    return raw_documents


def process_wikipedia_data(raw_documents):
    """
    Process (chunk and clean) the loaded Wikipedia data.
    This function is a mock since the actual module isn't available in this environment.
    """
    # Mocking the behavior of CharacterTextSplitter and other processing
    # Define chunking strategy
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000, chunk_overlap=20
    )
    # Chunk the document
    documents = text_splitter.split_documents(raw_documents)

    # Remove summary from metadata
    # LangChain’s WikipediaLoader adds a summary to each chunk by default. I thought the added summaries were a bit redundant. For example, if you used a vector similarity search to retrieve the top three results, the summary would be repeated three times. Therefore, I decided to remove it from the dataset.
    for d in documents:
        del d.metadata["summary"]

    return documents


# Modularizing Neo4j Data Storage
def store_data_in_neo4j(documents, credentials):
    """
    Store and index text with Neo4j.
    This function is a mock since the actual module isn't available in this environment.
    """
    # Neo4j Aura credentials
    url = credentials["url"]
    username = credentials["username"]
    password = credentials["password"]

    # OpenAI credentials
    openai_api_secret_key = credentials["openai_api_secret_key"]

    # Instantiate Neo4j vector from documents
    Neo4jVector.from_documents(
        documents,
        OpenAIEmbeddings(openai_api_key=openai_api_secret_key),
        url=url,
        username=username,
        password=password,
    )

    # Mocking the behavior of Neo4jVector and OpenAIEmbeddings
    stored_data = {"status": "Stored successfully", "count": len(documents)}
    return stored_data


# Load data from Wikipedia and store OpenAI embeddings in a Neo4j Vector
neo4j_credentials = {
    "url": env_vars["NEO4J_URI"],
    "username": env_vars["NEO4J_USERNAME"],
    "password": env_vars["NEO4J_PASSWORD"],
    "openai_api_secret_key": env_vars["OPEN_AI_SECRET_KEY"],
}

query = "Leonhard Euler"
raw_docs = load_wikipedia_data(query)
processed_docs = process_wikipedia_data(raw_docs)
storage_result = store_data_in_neo4j(processed_docs, neo4j_credentials)
