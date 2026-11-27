CREATE OR REPLACE VIEW v_kpis AS
SELECT
    (SELECT COUNT(*) FROM v_relevant_jobs)                 AS relevant_jobs,
    (SELECT COUNT(DISTINCT company) FROM v_relevant_jobs)  AS employers,
    (SELECT COUNT(DISTINCT skill) FROM skill_mention)      AS skills_found,
    (SELECT skill FROM v_top_skills LIMIT 1)               AS top_skill,
    (SELECT share_pct FROM v_top_skills LIMIT 1)           AS top_skill_pct,
    (SELECT MAX(fetched_at)::date FROM job_raw)            AS data_as_of;