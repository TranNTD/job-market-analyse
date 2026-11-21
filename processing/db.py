import os

import psycopg
from dotenv import load_dotenv

def get_connection() -> psycopg.Connection:
    """
    Establishes a connection to the PostgreSQL database using environment variables.

    Returns:
        psycopg.Connection: A connection object to the PostgreSQL database.
    """
    load_dotenv()  # Load environment variables from .env file
    variables = ["POSTGRES_HOST", "POSTGRES_PORT", "POSTGRES_DB", "POSTGRES_USER", "POSTGRES_PASSWORD"]

    # fail fast if any required environment variable is missing
    config = {}
    missing_vars  = []
    for var in variables:
        val = os.getenv(var)
        config[var] = val
        if val is None or val == "":
            missing_vars.append(var)
    if len(missing_vars) > 0:
        raise ValueError(f"Required environment variables {missing_vars} are not set.")

    # Establish and return the database connection
    return psycopg.connect(host=config["POSTGRES_HOST"]
                           , port=config["POSTGRES_PORT"]
                           , dbname=config["POSTGRES_DB"]
                           , user=config["POSTGRES_USER"]
                           , password=config["POSTGRES_PASSWORD"])