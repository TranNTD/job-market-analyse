import pytest

from processing.skills import SKILLS, find_skills

@pytest.mark.parametrize("text, expected", [
    ("Sehr gute SQL-Kenntnisse", {"SQL"}),
    ("Erfahrung mit Jira und Confluence", {"Jira", "Confluence"}),
    ("Power-BI und PowerBI und Power BI", {"Power BI"}),
    ("Anforderungsmanagement im Meldewesen", {"Requirements Engineering", "Regulatory Reporting"}),
    ("Arbeit im SAFe-Framework", {"SAFe"}),
    ("Erfahrung mit NoSQL-Datenbanken", {"SQL"}),
    ("MySQL, PostgreSQL oder SQLite", {"SQL"}),
    ("T-SQL und PL/SQL", {"SQL"}),
])

def test_finds_skills(text, expected):
    assert find_skills(text) == expected 

def test_every_skill_has_category_and_patterns():
    for name, skill in SKILLS.items():
        assert skill["category"], f"{name} has no category"
        assert skill["patterns"], f"{name} has no patterns"