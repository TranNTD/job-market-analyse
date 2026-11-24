
-- Only BA ads, each description only once - because skills come from descriptions
CREATE OR REPLACE VIEW v_relevant_jobs AS
SELECT DISTINCT ON (md5(description))
    id, refnr, title, company, description
FROM job_raw
WHERE title ILIKE '%business analy%'
    AND description IS NOT NULL
ORDER BY md5(description), id;

-- v_top_skills with relevant only ads
CREATE OR REPLACE VIEW v_top_skills AS
SELECT 
    skill,
    category,
    COUNT(DISTINCT job_id) AS job_count,
    ROUND(100*COUNT(DISTINCT job_id) / (SELECT COUNT(*) FROM v_relevant_jobs), 1) AS share_pct
FROM skill_mention
GROUP BY skill, category
ORDER BY job_count DESC;