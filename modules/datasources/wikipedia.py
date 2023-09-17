from langchain.document_loaders import WikipediaLoader
from langchain.text_splitter import CharacterTextSplitter


def load_wikipedia_data(query: str):
    """
    Load data from Wikipedia based on the given query.
    This function is a mock since the actual module isn't available in this environment.
    """
    # Reading and chunking a Wikipedia article
    # https://neo4j.com/developer-blog/langchain-library-full-support-neo4j-vector-index/

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
