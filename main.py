from modules.environment.environment_utilities import (
    load_environment_variables,
    verify_environment_variables,
)


def load_data_from_wikipedia_and_store_openai_embeddings_in_neo4j_vector():
    try:
        print(
            f"Loading data from Wikipedia and store OpenAI embeddings in a Neo4j Vector"
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def query_against_an_existing_neo4j_vector():
    try:
        print(f"Query against an existing Neo4j Vector")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def question_answer_workflow_with_langchain():
    try:
        print(f"Question-Answer Workflow With LangChain")
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
