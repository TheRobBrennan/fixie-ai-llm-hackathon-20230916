# Import required modules and utility functions

from environment_utilities import (
    load_environment_variables,
    verify_environment_variables,
)
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


def initialize_neo4j_vector(credentials, index_name):
    """
    Function to instantiate a Neo4j vector from an existing vector.
    """
    # Implement the actual logic using the langchain and neo4j modules here
    # Neo4j Aura credentials
    url = credentials["url"]
    username = credentials["username"]
    password = credentials["password"]

    # OpenAI credentials
    openai_api_secret_key = credentials["openai_api_secret_key"]

    # Instantiate Neo4j vector from an existing vector
    # CYPHER - "SHOW INDEXES;" will show we have an index type Vector named "vector"
    neo4j_vector = Neo4jVector.from_existing_index(
        OpenAIEmbeddings(openai_api_key=openai_api_secret_key),
        url=url,
        username=username,
        password=password,
        index_name=index_name,
    )

    return neo4j_vector


def initialize_qa_workflow(neo4j_vector, openai_api_secret_key):
    """
    Function to set up the question-answer workflow using LangChain.
    """
    # Implement the actual logic using the langchain modules here
    chain = RetrievalQAWithSourcesChain.from_chain_type(
        ChatOpenAI(temperature=0, openai_api_key=openai_api_secret_key),
        chain_type="stuff",
        retriever=neo4j_vector.as_retriever(),
    )

    return chain


def execute_qa_workflow(qa_workflow, query, openai_api_secret_key):
    """
    Function to execute the QA workflow and retrieve the answers.
    """
    # Implement the actual logic using the qa_workflow
    qa_workflow(
        {"question": query},
        return_only_outputs=True,
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(temperature=0, openai_api_key=openai_api_secret_key),
        neo4j_vector.as_retriever(),
        memory=memory,
    )
    # results = qa({"question": query})["answer"]
    results = qa({"question": query})

    return results


# Main Execution

# Load and verify environment variables using the utility
env_vars = load_environment_variables()
if not verify_environment_variables(env_vars):
    raise ValueError("Some environment variables are missing!")

# Verify the environment variables
if not verify_environment_variables(env_vars):
    raise ValueError("Some environment variables are missing!")

# Initialize the Neo4j vector
credentials = {
    "url": env_vars["NEO4J_URI"],
    "username": env_vars["NEO4J_USERNAME"],
    "password": env_vars["NEO4J_PASSWORD"],
    "openai_api_secret_key": env_vars["OPEN_AI_SECRET_KEY"],
}
index_name = "vector"  # default index name
neo4j_vector = initialize_neo4j_vector(credentials, index_name)

# Initialize and execute the QA workflow
qa_workflow = initialize_qa_workflow(neo4j_vector, env_vars["OPEN_AI_SECRET_KEY"])
query = "What is Euler credited for popularizing?"
qa_results = execute_qa_workflow(qa_workflow, query, env_vars["OPEN_AI_SECRET_KEY"])
# print(qa_results)
print(qa_results["answer"])

# Close the Neo4j connection (if a close method is available)
neo4j_vector._driver.close()
