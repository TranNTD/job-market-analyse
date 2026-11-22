--- Step 1: tables for jobs ads and skill mentions

CREATE TABLE IF NOT EXISTS job_raw (
    id SERIAL PRIMARY KEY,
    refnr TEXT NOT NULL UNIQUE, -- prevent duplicates
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT,
    description TEXT,
    published_at DATE,
    fetched_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS skill_mention (
    job_id INTEGER NOT NULL REFERENCES job_raw(id) ON DELETE CASCADE, -- foreign key, if an ad is deleted its skill mentions are deleted too
    skill TEXT NOT NULL,
    category TEXT NOT NULL,
    PRIMARY KEY (job_id, skill)
);


