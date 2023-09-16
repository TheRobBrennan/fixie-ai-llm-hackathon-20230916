from modules.environment.environment_utilities import (
    load_environment_variables,
    verify_environment_variables,
)

try:
    # Load environment variables using the utility
    env_vars = load_environment_variables()

    # Verify the environment variables
    if not verify_environment_variables(env_vars):
        raise ValueError("Some environment variables are missing!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
