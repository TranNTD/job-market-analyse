![CI](https://github.com/TranNTD/job-market-analyse/actions/workflows/ci.yml/badge.svg)
# Job-Market-Analyse: Skills für Business Analysts in der Finanzbranche

Dieses Projekt sammelt aktuelle Stellenanzeigen für Business Analysts im Raum Frankfurt,
erkennt darin automatisch geforderte Skills (Tools, Methoden, Fachwissen, Sprachen) und
erstellt daraus einen Bericht als PDF oder PowerPoint.

Die Frage dahinter: **Welche Skills werden in der Finanzbranche von Business Analysts am häufigsten verlangt?**

## Ergebnis

Der Bericht enthält:
- die Anzahl der ausgewerteten Anzeigen,
- ein Balkendiagramm der Top-Skills (Anteil der Anzeigen in %),
- eine Tabelle aller erkannten Skills mit Kategorie und Häufigkeit.

> **Hinweis:** Die aktuelle Datenbasis ist noch klein (einstellige bis niedrige zweistellige Anzahl relevanter Anzeigen).
> Die Prozentwerte sind daher als erste Tendenz zu lesen, nicht als repräsentative Aussage.

## Architektur

![Pipeline](docs/architecture/pipeline.png)

| Schritt | Was passiert | Technik |
|---|---|---|
| 1. Sammeln | Stellenanzeigen von Indeed abrufen und als datierte CSV speichern | Python, [JobSpy](https://github.com/speedyapply/JobSpy) |
| 2. Speichern | CSV-Dateien idempotent in die Datenbank laden (keine Dubletten) | Python, pandas, psycopg, PostgreSQL in Docker |
| 3. Auswerten | Relevante Anzeigen filtern (Titel enthält „Business Analy“, Dubletten per Text-Hash entfernt), Skills per Wörterbuch und regulären Ausdrücken erkennen | Python (regex), SQL-Views |
| 4. Berichten | Bericht aus den Views erzeugen, als PDF oder PPTX | Java, Eclipse BIRT (ReportEngine) |
| Automatisierung | Schritte 2–4 mit einem Befehl | PowerShell (`run_pipeline.ps1`) |

## Tech-Stack

| Bereich | Werkzeuge |
|---|---|
| Datenerfassung & Verarbeitung | Python 3.12, pandas, python-jobspy, psycopg 3, python-dotenv |
| Datenbank | PostgreSQL 17 (Docker Compose) |
| Bericht | Java 21, Eclipse BIRT 4.25 (Report Designer + Runtime), PostgreSQL-JDBC-Treiber |
| Tests | pytest (Unit- und Integrationstests mit Rollback) |
| Versionierung | Git, GitHub (Issues, Pull Requests, Tags) |

## Voraussetzungen

- Docker Desktop
- Python 3.12+
- JDK 21 (z. B. Eclipse Temurin)
- BIRT Runtime 4.25 (`birt-runtime-4.25.0-….zip`, entpackt)
- PostgreSQL-JDBC-Treiber (`postgresql-42.x.x.jar`)
- Optional: BIRT Report Designer, um den Bericht zu bearbeiten

## Setup

```powershell
# 1. Repo klonen
git clone https://github.com/TranNTD/job-market-analyse.git
cd job-market-analyse

# 2. Zugangsdaten: .env aus der Vorlage erstellen und Passwort setzen
Copy-Item .env.example .env

# 3. Datenbank starten und Tabellen/Views anlegen
docker compose up -d
Get-Content sql\001_schema.sql, sql\002_views.sql, sql\003_add_source_columns.sql, sql\004_relevant_jobs.sql |
    docker exec -i ba_jobs_db psql -U ba_user -d ba_jobs

# 4. Python-Umgebung anlegen und Pakete installieren
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 5. Tests ausführen (Datenbank muss laufen)
pytest -v
```

**Bericht:** In `report/run_report.ps1` die Pfade zur BIRT Runtime und zum JDBC-Treiber an den eigenen Rechner anpassen.

## Benutzung