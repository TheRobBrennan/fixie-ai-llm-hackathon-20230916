from environment_utilities import (
    load_environment_variables,
    verify_environment_variables,
)
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings.openai import OpenAIEmbeddings

# Load and verify environment variables using the utility
env_vars = load_environment_variables()
if not verify_environment_variables(env_vars):
    raise ValueError("Some environment variables are missing!")

# Verify the environment variables
if not verify_environment_variables(env_vars):
    raise ValueError("Some environment variables are missing!")


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


def perform_similarity_search(neo4j_vector, query):
    """
    Function to perform a vector similarity search.
    """
    # Implement the actual logic using the langchain module's similarity_search method
    try:
        results = neo4j_vector.similarity_search(query)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return results


# Main Execution
try:
    # Initialize the Neo4j vector
    credentials = {
        "url": env_vars["NEO4J_URI"],
        "username": env_vars["NEO4J_USERNAME"],
        "password": env_vars["NEO4J_PASSWORD"],
        "openai_api_secret_key": env_vars["OPEN_AI_SECRET_KEY"],
    }
    # Instantiate Neo4j vector from an existing vector
    # CYPHER - "SHOW INDEXES;" will show we have an index type Vector named "vector"
    index_name = "vector"  # default index name
    neo4j_vector = initialize_neo4j_vector(credentials, index_name)

    # Perform the similarity search and display results
    query = "Where did Euler grow up?"
    results = perform_similarity_search(neo4j_vector, query)

    # Close the driver
    neo4j_vector._driver.close()

    # Do something with the results
    # print(results)
    print(results[0].page_content)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
