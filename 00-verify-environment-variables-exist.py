import os
from environs import Env

env = Env()
env.read_env()  # reads .env file

# Define a dictionary of expected environment variables
env_vars = {
    "OPEN_AI_SECRET_KEY": None,
    "NEO4J_URI": None,
    "NEO4J_USERNAME": None,
    "NEO4J_PASSWORD": None,
    "AURA_INSTANCEID": None,
    "AURA_INSTANCENAME": None,
}

# Load environment variables from .env into the dictionary
for key in env_vars:
    env_vars[key] = os.environ.get(key)

# Check to make sure we have all of our expected environment variables defined
all_env_vars_set = True

for key, value in env_vars.items():
    if not value:
        print(f"{key} is not set!")
        all_env_vars_set = False

if all_env_vars_set:
    print("All environment variables have been defined correctly!")
