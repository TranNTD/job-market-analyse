import pandas as pd 
import numpy as np
from datetime import datetime as dt
from pathlib import Path

DATA_DIR = Path("data/raw")

def latest_csv() -> Path:
    """Returns the most recent jobs_*.csv in data/."""
    files = sorted(DATA_DIR.glob("jobs_*.csv"))
    if not files:
        raise FileNotFoundError("No jobs_*.csv found in data/")
    return files[-1]

path = latest_csv()
print(f"Checking {path.name}")
data = pd.read_csv(f"{path}")
data = data.astype(object).where(data.notna(), None)


if __name__ == "__main__":
    
    print(data.isna().sum())
    print(data["site"].value_counts())
    print(data[["title", "company"]])
    print(data.groupby("site")["description"].apply(lambda s: s.notna().sum()))
