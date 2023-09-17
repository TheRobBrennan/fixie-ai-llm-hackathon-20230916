# Welcome

This project will explore my adventures at today's Fixie AI + LLM Hackathon.

Let's take a trip to Python land and see how to get started exploring how to incorporate Neo4j with an LLM application.

If this is your first time setting up this project and related resources, please see the `Initial setup` section below.

If you've already set up your OpenAI, Neo4j, and Python virtual environment, you can run the project:

```sh
# Activate your virtual environment
% source .venv/bin/activate
(.venv) %

# Load your environment variables (defined in ".env")
(.venv) % source .env

# Run the main script
(.venv) % python3 main.py

Load data from Wikipedia and store OpenAI embeddings in a Neo4j Vector
	Query: Leonhard Euler

Created a chunk of size 1124, which is longer than the specified 1000
Created a chunk of size 1221, which is longer than the specified 1000

Query against an existing Neo4j Vector
	Query: Where did Euler grow up?

== Early life ==
Leonhard Euler was born on 15 April 1707, in Basel, Switzerland, to Paul III Euler, a pastor of the Reformed Church, and Marguerite (née Brucker), whose ancestors include a number of well-known scholars in the classics. He was the oldest of

Question/Answer workflow with LangChain
	Query: What is Euler credited for popularizing?

Euler is credited for popularizing several mathematical concepts and notations. Some of the things he is credited for popularizing include:

1. The use of the Greek letter π (pi) to represent the ratio of a circle's circumference to its diameter.
2. The notation f(x) to represent a function.
3. The use of the letter e to represent the base of the natural logarithm, now known as Euler's number.
4. The use of the letter i to represent the imaginary unit (√-1).
5. The use of lowercase letters to represent the sides of a triangle and uppercase letters to represent the angles.
6. The use of the Greek letter Σ (sigma) to represent summations.
7. The use of the Greek letter Δ (delta) to represent finite differences.

These are just a few examples of the many mathematical concepts and notations that Euler is credited for popularizing.
```

Shout-out to [LangChain Library Adds Full Support for Neo4j Vector Index](https://neo4j.com/developer-blog/langchain-library-full-support-neo4j-vector-index/) for serving as a great guide for getting started with Neo4j Vectors. This project has been refactored for a more modular approach - and includes a few tweaks based on my personal taste.

## Initial setup

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

Once you have your environment variables defined and your Python virtual environment activated, you can use `source` to load them into your terminal/shell:

```sh
# Activate your virtual environment
% source .venv/bin/activate
(.venv) % source .env
```

At this point, you can either use Google Colab to open the notebook hosted on GitHub at [https://github.com/tomasonjo/blogs/blob/master/llm/official_langchain_neo4jvector.ipynb](https://github.com/tomasonjo/blogs/blob/master/llm/official_langchain_neo4jvector.ipynb) - or you can start developing in Python locally.

For this experiment, I'm going to develop locally in Python - using a simple Python starter I created at [https://github.com/TheRobBrennan/explore-python](https://github.com/TheRobBrennan/explore-python). See [./GETTING-STARTED-WITH-PYTHON-AND-VS-CODE.md](./GETTING-STARTED-WITH-PYTHON-AND-VS-CODE.md) for more details on getting that set up.

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
(.venv) % pip install langchain openai wikipedia tiktoken neo4j
# ... continue to install packages as needed ...
#
#       - OR -
#
# Install the packages from requirements.txt
(.venv) % pip install -r requirements.txt
```

For completeness, the following commands are helpful when working with a Python project:

```sh
# When you are ready to generate a requirements.txt file
# % pip freeze > requirements.txt

# What happens if you want to uninstall a package?

# Uninstall the package from your virtual environment
# % pip uninstall simplejson

# Remove the dependency from requirements.txt if it exists
# % pip uninstall -r requirements.txt
```
