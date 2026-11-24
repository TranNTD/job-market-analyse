ALTER TABLE job_raw
    ADD COLUMN IF NOT EXISTS source           TEXT,
    ADD COLUMN IF NOT EXISTS job_url          TEXT,
    ADD COLUMN IF NOT EXISTS company_industry TEXT;