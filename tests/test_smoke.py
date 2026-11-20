from processing.db import get_connection

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