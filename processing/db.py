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

    # Retrieve database connection parameters from environment variables
    db_host = os.getenv("POSTGRES_HOST")
    db_port = os.getenv("POSTGRES_PORT")
    db_name = os.getenv("POSTGRES_DB")
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")

    # Create a connection string
    conn_str = f"host={db_host} port={db_port} dbname={db_name} user={db_user} password={db_password}"

    # Establish and return the database connection
    return psycopg.connect(conn_str)