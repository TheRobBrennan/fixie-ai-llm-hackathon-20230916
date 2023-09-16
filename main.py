from modules.environment.environment_utilities import (
    load_environment_variables,
    verify_environment_variables,
)
from modules.datasources.wikipedia import load_wikipedia_data, process_wikipedia_data
from modules.langchain.langchain import initialize_qa_workflow, execute_qa_workflow
from modules.neo4j.credentials import neo4j_credentials
from modules.neo4j.vector import (
    store_data_in_neo4j,
    initialize_neo4j_vector,
    perform_similarity_search,
)


def load_data_from_wikipedia_and_store_openai_embeddings_in_neo4j_vector():
    try:
        print(f"Load data from Wikipedia and store OpenAI embeddings in a Neo4j Vector")

        query = "Leonhard Euler"
        raw_docs = load_wikipedia_data(query)
        processed_docs = process_wikipedia_data(raw_docs)
        store_data_in_neo4j(processed_docs, neo4j_credentials)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def query_against_an_existing_neo4j_vector():
    try:
        print(f"Query against an existing Neo4j Vector")

        # Instantiate Neo4j vector from an existing vector
        # CYPHER - "SHOW INDEXES;" will show we have an index type Vector named "vector"
        index_name = "vector"  # default index name
        neo4j_vector = initialize_neo4j_vector(neo4j_credentials, index_name)

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


def question_answer_workflow_with_langchain():
    try:
        print(f"Question-Answer Workflow With LangChain")

        index_name = "vector"  # default index name
        neo4j_vector = initialize_neo4j_vector(neo4j_credentials, index_name)

        # Initialize and execute the QA workflow
        qa_workflow = initialize_qa_workflow(
            neo4j_vector, neo4j_credentials["openai_api_secret_key"]
        )
        query = "What is Euler credited for popularizing?"
        qa_results = execute_qa_workflow(
            neo4j_vector, qa_workflow, query, neo4j_credentials["openai_api_secret_key"]
        )
        # print(qa_results)
        print(qa_results["answer"])

        # Close the Neo4j connection (if a close method is available)
        neo4j_vector._driver.close()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main program
try:
    # Load environment variables using the utility
    env_vars = load_environment_variables()

    # Verify the environment variables
    if not verify_environment_variables(env_vars):
        raise ValueError("Some environment variables are missing!")

    # Here we go!
    load_data_from_wikipedia_and_store_openai_embeddings_in_neo4j_vector()
    query_against_an_existing_neo4j_vector()
    question_answer_workflow_with_langchain()

except Exception as e:
    print(f"An unexpected error occurred: {e}")
