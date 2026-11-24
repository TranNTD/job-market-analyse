from pathlib import Path

import pandas as pd

from processing.db import get_connection

DATA_DIR = Path("data/raw")

# CSV column → order must match INSERT_SQL
CSV_COLUMNS = ["id", "title", "company", "location", "description",
               "date_posted", "site", "job_url", "company_industry"]

INSERT_SQL = """
    INSERT INTO job_raw (refnr, title, company, location, description,
                         published_at, source, job_url, company_industry)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (refnr) DO NOTHING
"""


def read_csv(path: Path) -> pd.DataFrame:
    """Reads one CSV and replaces missing values (NaN) with None."""
    data = pd.read_csv(f"{path}")
    data = data[CSV_COLUMNS] # change column order to fit table-structure in database  
    data = data.astype(object).where(data.notna(), None)
    return data  

def load_file(conn, path: Path) -> tuple[int, int]:
    """takes one CSV file and writes its rows into job_raw. At the end it reports how many ads were new and how many were already there."""
    inserted = skipped = 0
    df = read_csv(path)

    for row in df.itertuples(index=False, name=None):
        cur = conn.execute(INSERT_SQL, row)
        if cur.rowcount == 1:
            inserted += 1
        else:
            skipped += 1
    return inserted, skipped


def main() -> None:
    files = sorted(DATA_DIR.glob("jobs_*.csv"))
    if not files:
        print("No CSV files found in data/")
        return

    with get_connection() as conn:
        for path in files:
            inserted, skipped = load_file(conn, path)
            print(f"{path.name}: {inserted} inserted, {skipped} skipped")

if __name__ == "__main__":
    main()

# DATA_DIR = Path("data/raw")

# def latest_csv() -> Path:
#     """Returns the most recent jobs_*.csv in data/."""
#     files = sorted(DATA_DIR.glob("jobs_*.csv"))
#     if not files:
#         raise FileNotFoundError("No jobs_*.csv found in data/")
#     return files[-1]

# path = latest_csv()
# print(f"Checking {path.name}")



# if __name__ == "__main__":
    
#     print(data.isna().sum())
#     print(data["site"].value_counts())
#     print(data[["title", "company"]])
#     print(data.groupby("site")["description"].apply(lambda s: s.notna().sum()))
