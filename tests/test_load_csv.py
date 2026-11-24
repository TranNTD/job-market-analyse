import pandas as pd
from processing.db import get_connection
from ingestion.load_csv import CSV_COLUMNS, load_file, read_csv


def write_test_csv(path, rows):
    pd.DataFrame(rows, columns=CSV_COLUMNS).to_csv(path, index=False)


def make_row(refnr, title="Business Analyst", industry=None):
    """One test ad. Only refnr, title and industry vary, the rest is fixed."""
    return {
        "id": refnr,
        "title": title,
        "company": "MOCK GmbH",
        "location": "Frankfurt",
        "description": "Erfahrung mit SQL und Jira",
        "date_posted": "2026-11-23",
        "site": "indeed",
        "job_url": f"https://example.com/{refnr}",
        "company_industry": industry,
    }


# ---------- Unit tests: no database needed ----------

def test_read_csv_replaces_nan_with_none(tmp_path):
    path = tmp_path / "jobs_test.csv"
    write_test_csv(path, [make_row("TEST-1", industry=None)])

    df = read_csv(path)

    assert df.loc[0, "company_industry"] is None


def test_read_csv_keeps_only_needed_columns(tmp_path):
    path = tmp_path / "jobs_test.csv"
    row = make_row("TEST-1")
    row["salary"] = 50000                      # extra column that should be dropped
    pd.DataFrame([row]).to_csv(path, index=False)

    df = read_csv(path)

    assert set(list(df.columns)) == set(CSV_COLUMNS)


# ---------- Integration tests: use the real database, then roll back ----------

def test_load_file_inserts_new_rows(db_conn, tmp_path):
    # Arrange: a CSV with two new ads
    path = tmp_path / "jobs_test.csv"
    write_test_csv(path, [make_row("TEST-1"), make_row("TEST-2")])

    # Act
    inserted, skipped = load_file(db_conn, path)

    # Assert: the counters and the database content
    assert (inserted, skipped) == (2, 0)
    count = db_conn.execute(
        "SELECT COUNT(*) FROM job_raw WHERE refnr LIKE 'TEST-%'"
    ).fetchone()[0]
    assert count == 2


def test_load_file_is_idempotent(db_conn, tmp_path):
    path = tmp_path / "jobs_test.csv"
    write_test_csv(path, [make_row("TEST-1"), make_row("TEST-2")])

    load_file(db_conn, path)                   # first run
    inserted, skipped = load_file(db_conn, path)  # second run, same file

    assert (inserted, skipped) == (0, 2)


def test_load_file_stores_missing_values_as_null(db_conn, tmp_path):
    path = tmp_path / "jobs_test.csv"
    write_test_csv(path, [make_row("TEST-1", industry=None)])

    load_file(db_conn, path)

    row = db_conn.execute(
    "SELECT company_industry FROM job_raw WHERE refnr = %s",
    ("TEST-1",),
    ).fetchone()
    assert row is not None, "TEST-1 was not inserted"
    assert row[0] is None

def test_read_csv_reorders_columns(tmp_path):
    path = tmp_path / "jobs_test.csv"
    row = make_row("TEST-1")
    shuffled = list(reversed(CSV_COLUMNS))
    pd.DataFrame([row])[shuffled].to_csv(path, index=False)

    df = read_csv(path)

    assert list(df.columns) == CSV_COLUMNS