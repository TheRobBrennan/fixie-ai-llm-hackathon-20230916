# Welcome

This project will explore my adventures at today's Fixie AI + LLM Hackathon.

## Experiment 01

Let's take a trip to Python land and see how to get started exploring how to incorporate Neo4j with an LLM application.

### Scratchpad

Initial setup:

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

### Resources

- [LangChain Library Adds Full Support for Neo4j Vector Index](https://neo4j.com/developer-blog/langchain-library-full-support-neo4j-vector-index/)
