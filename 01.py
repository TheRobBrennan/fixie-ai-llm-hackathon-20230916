import os
from environs import Env
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.document_loaders import WikipediaLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# Read our .env file
env = Env()
env.read_env()

# Reading and chunking a Wikipedia article
# https://neo4j.com/developer-blog/langchain-library-full-support-neo4j-vector-index/

# Read the wikipedia article
raw_documents = WikipediaLoader(query="Leonhard Euler").load()
# Define chunking strategy
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=20
)
# Chunk the document
documents = text_splitter.split_documents(raw_documents)

# Remove summary from metadata
for d in documents:
    del d.metadata["summary"]
