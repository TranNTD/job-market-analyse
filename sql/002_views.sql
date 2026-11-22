-- the view show how many ads mention each skill and what percentage of all ads that is.
-- required columns: skill, category, job_count, share_pct

CREATE OR REPLACE VIEW v_top_skills AS
SELECT
    skill,
    category,
    COUNT(job_id) AS job_count,
    ROUND(100 * COUNT(DISTINCT job_id)/(SELECT COUNT(*) FROM job_raw),1) as share_pct
FROM skill_mention
GROUP BY skill, category
ORDER BY job_count DESC;