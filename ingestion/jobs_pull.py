from jobspy import scrape_jobs

from pathlib import Path
from datetime import datetime as dt
import pandas as pd


SEARCH_TERMS = ["business analyst bank", "business analyst finance",
                "business analyst versicherung", "business analyst"]

all_jobs = []
for term in SEARCH_TERMS:
    all_jobs.append(scrape_jobs(
        site_name=["indeed"],
        search_term=term,
        location="Frankfurt am Main",
        distance=100,
        results_wanted=100,
        hours_old=168,
        country_indeed="Germany",
    ))
jobs = pd.concat(all_jobs).drop_duplicates(subset="id")
print(f"Found {len(jobs)} jobs")
print(jobs[["site", "title", "company", "location"]])

# Extract only needed parameters
pull_time = dt.today().strftime("%Y-%m-%d-%H%M%S")
Path("data/raw").mkdir(exist_ok=True)
needed_params = ["id", "title", "company", "location", "date_posted", "description", "site", "job_url", "company_industry"]
jobs[needed_params].to_csv(f"data/raw/jobs_{pull_time}.csv", index=False)