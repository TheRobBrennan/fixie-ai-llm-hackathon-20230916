# Welcome

This project will explore my adventures at today's Fixie AI + LLM Hackathon.

## Experiment 01

Let's take a trip to Python land and see how to get started exploring how to incorporate Neo4j with an LLM application.

### Scratchpad

#### Initial setup

- OpenAI
  - Create an OpenAI API key
  - Be sure to define the following environment variables in `.env`
    - `OPEN_AI_SECRET_KEY`
- Neo4j Environment Setup
  - Create a new (free) instance on Aura
    - Be sure to define the following environment variables in `.env`
      - `NEO4J_URI`
      - `NEO4J_USERNAME`
      - `NEO4J_PASSWORD`
      - `AURA_INSTANCEID`
      - `AURA_INSTANCENAME`

Once you have your environment variables defined, you can use `source` to load them into your terminal/shell:
`% source .env`

At this point, you can either use Google Colab to open the notebook hosted on GitHub at [https://github.com/tomasonjo/blogs/blob/master/llm/official_langchain_neo4jvector.ipynb](https://github.com/tomasonjo/blogs/blob/master/llm/official_langchain_neo4jvector.ipynb) - or you can start developing in Python locally.

For this experiment, I'm going to develop locally in Python - using a simple Python starter I created at [https://github.com/TheRobBrennan/explore-python](https://github.com/TheRobBrennan/explore-python). See [./GETTING-STARTED-WITH-PYTHON-AND-VS-CODE.md](./GETTING-STARTED-WITH-PYTHON-AND-VS-CODE.md) for more details on getting that set up.

You should be able to run `python3 ./explore-python/hello-world.py` and optionally use the VS Code debugger before moving on.

### Resources

- [LangChain Library Adds Full Support for Neo4j Vector Index](https://neo4j.com/developer-blog/langchain-library-full-support-neo4j-vector-index/)
