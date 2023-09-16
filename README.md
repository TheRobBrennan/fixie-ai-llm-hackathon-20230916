# Welcome

This project will explore my adventures at today's Fixie AI + LLM Hackathon.

## Experiment 01

Let's take a trip to Python land and see how to get started exploring how to incorporate Neo4j with an LLM application.

### Resources

- [LangChain Library Adds Full Support for Neo4j Vector Index](https://neo4j.com/developer-blog/langchain-library-full-support-neo4j-vector-index/)

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

You should be able to run `python3 ./hello-world.py` and optionally use the VS Code debugger before moving on.

```sh
# Verify that you have Python installed on your machine
% python3 --version
Python 3.11.1

# Create a new virtual environment for the project
% python3 -m venv .venv

# Select your new environment by using the Python: Select Interpreter command in VS Code
#   - Enter the path: ./.venv/bin/python

# Activate your virtual environment
% source .venv/bin/activate
(.venv) %

# Install Python packages in a virtual environment
# % pip install langchain openai wikipedia tiktoken neo4j
# ... continue to install packages as needed ...

# When you are ready to generate a requirements.txt file
# % pip freeze > requirements.txt

# What happens if you want to uninstall a package?

# Uninstall the package from your virtual environment
# % pip uninstall simplejson

# Remove the dependency from requirements.txt if it exists
# % pip uninstall -r requirements.txt

# Install the packages from requirements.txt
(.venv) % pip install -r requirements.txt
```

#### Step 00 - Verify that you have your environment variables defined

```sh
% python3 00-verify-environment-variables-exist.py
All environment variables have been defined correctly!
```

#### Step 01 - Load data from Wikipedia and store OpenAI embeddings in a Neo4j Vector

```sh
% python3 01-load-data-from-wikipedia-and-store-openai-embeddings-in-neo4j-vector.py
Created a chunk of size 1124, which is longer than the specified 1000
Created a chunk of size 1221, which is longer than the specified 1000
== Early life ==
Leonhard Euler was born on 15 April 1707, in Basel, Switzerland, to Paul III Euler, a pastor of the Reformed Church, and Marguerite (née Brucker), whose ancestors include a number of well-known scholars in the classics. He was the oldest of
```

#### Step 02 - Query against an existing Neo4j Vector

Now that we have our data stored in the Neo4j database, let's see how we can run a query against it:

```sh
% python3 02-verify-query-against-neo4j-vector.py
== Early life ==
Leonhard Euler was born on 15 April 1707, in Basel, Switzerland, to Paul III Euler, a pastor of the Reformed Church, and Marguerite (née Brucker), whose ancestors include a number of well-known scholars in the classics. He was the oldest of
```
