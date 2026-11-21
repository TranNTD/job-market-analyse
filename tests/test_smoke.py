from processing.db import get_connection
import pytest

def test_pytest_works():
    """
    A simple test to verify that pytest is working correctly.
    """
    a = 1 + 1
    assert a == 2, "Basic arithmetic failed: 1 + 1 should equal 2"

def test_db_connection():
    """
    Test to verify that a connection to the PostgreSQL database can be established.
    """
    try:
        with get_connection() as conn:
            result = conn.execute("SELECT 1;")
            assert result.fetchone()[0] == 1
    except Exception as e:
        assert False, f"Database connection test failed with error: {e}"

REQUIRED_ENV_VARS = ["POSTGRES_HOST", "POSTGRES_PORT", "POSTGRES_DB", "POSTGRES_USER", "POSTGRES_PASSWORD"]

@pytest.mark.parametrize("var", REQUIRED_ENV_VARS)
def test_missing_env_vars(monkeypatch, var):
    """
    Test to verify that the get_connection function raises an error when required environment variables are missing.
    """
    # Clear environment variables
    monkeypatch.setenv(var, "")

    with pytest.raises(ValueError, match = var):
        get_connection()