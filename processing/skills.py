
"""
For each skill, we store a canonical name (how it appears in the report), 
a category, and search patterns, which are the different ways companies write it
"""
import re

# canonical name → category, search patterns (regular expressions), case-sensitive?
SKILLS = {
    # --- Tools ---
    "SQL":        {"category": "Tools", "patterns": [r"\w*sql\w*"]},
    "Excel":      {"category": "Tools", "patterns": [r"excel"]},
    "Power BI":   {"category": "Tools", "patterns": [r"power[\s-]?bi"]},
    "Jira":       {"category": "Tools", "patterns": [r"jira"]},
    "Confluence": {"category": "Tools", "patterns": [r"confluence"]},
    "Python":     {"category": "Tools", "patterns": [r"python"]},
    "SAP":        {"category": "Tools", "patterns": [r"sap"]},
    "Tableau":    {"category": "Tools", "patterns": [r"tableau"]},
    "Databricks": {"category": "Tools", "patterns": [r"databricks"]},
    "R": {"category": "Tools",
      "patterns": [r"R-Programmierung", r"Programmiersprache R", r"RStudio", r"Python(?:,| und| or| oder) R"],
      "case_sensitive": True},
    "Java":        {"category": "Tools", "patterns": [r"java"]},
    
    # --- Technology ---
    "AI": {"category": "Technology",
       "patterns": [r"KI", r"AI", r"künstliche[rn]? Intelligenz", r"artificial intelligence",
                    r"LLMs?", r"machine learning"],
       "case_sensitive": True},

    # --- Methods ---
    "Requirements Engineering": {
        "category": "Methods",
        "patterns": [r"requirements?[\s-]engineering", r"anforderungsmanagement", r"anforderungsanalyse"],
    },
    "Process Analysis": {"category": "Methods",
                     "patterns": [r"prozessanalyse\w*", r"prozessmodellierung", r"process analysis",
                                  r"process model(?:l)?ing"]},
    "User Stories": {"category": "Methods", "patterns": [r"user[\s-]stor(?:y|ies)"]},
    "Scrum":        {"category": "Methods", "patterns": [r"scrum"]},
    "SAFe":         {"category": "Methods", "patterns": [r"SAFe"], "case_sensitive": True},

    # --- Domain knowledge ---
    "Regulatory Reporting": {
        "category": "Domain",
        "patterns": [r"meldewesen", r"regulatory reporting", r"regulatorische[sn]? reporting"],
    },
    "Reporting": {"category": "Methods",
              "patterns": [r"reporting", r"berichtswesen", r"bericht(?:e|erstattung)?"]},
    "Presentation": {"category": "Soft Skills",
                 "patterns": [r"präsentation\w*", r"presentation skills"]},
    # --- Soft Skills ----
    "Communication": {
        "category": "Soft Skills",
        "patterns":[r"kommunikationsstärke", r"kommunikationsfähigkeit\w*", r"communication skills"]
    },
    # --- Languages ---
    "German":  {"category": "Languages", "patterns": [r"deutsch", r"german"]},
    "English": {"category": "Languages", "patterns": [r"englisch", r"english"]},

}


def _compile(skill: dict) -> re.Pattern:
    """Builds one regex from all patterns of a skill, with word boundaries."""
    flags = 0 if skill.get("case_sensitive") else re.IGNORECASE
    return re.compile(r"\b(?:" + "|".join(skill["patterns"]) + r")\b", flags)


# Compile once when the module is loaded, not again for every ad
_COMPILED = {name: _compile(skill) for name, skill in SKILLS.items()}


def find_skills(text: str | None) -> set[str]:
    """Returns the canonical names of all skills found in the text."""
    if text == "" or text is None:
        return set()
    return {name for name, pattern in _COMPILED.items() if pattern.search(text)}
        