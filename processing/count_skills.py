from processing.db import get_connection
from processing.skills import SKILLS, find_skills

INSERT_SQL = """
    INSERT INTO skill_mention (job_id, skill, category)
    VALUES (%s, %s, %s)
    ON CONFLICT (job_id, skill) DO NOTHING
"""


def main() -> None:
    with get_connection() as conn:
        jobs = conn.execute("SELECT id, description FROM v_relevant_jobs").fetchall()

        # Recalculate from scratch every time, so changes to SKILLS are always reflected
        conn.execute("TRUNCATE skill_mention")

        mentions = 0
        for job_id, description in jobs:
            for skill in find_skills(description):
                conn.execute(INSERT_SQL, (job_id, skill, SKILLS[skill]["category"]))
                mentions += 1

        print(f"{len(jobs)} relevant ads analysed, {mentions} skill mentions stored")


if __name__ == "__main__":
    main()