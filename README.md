# Job-Market-Analyse: Skills für Business Analysts in der Finanzbranche

Dieses Projekt benutzt Scrape_job um alle mögliche relevante Job zu sammeln und weiter mit LLM alle nötige Skills in Beschreibungen extrahieren. Am Ende der Pipeline sind Output in PDF oder PPTX format.

## Architektur
![Pipeline](docs/architecture/pipeline.png)

- Sammeln und Verarbeiten mit python Scrape_Job
- Speichern in PostgreSQL (JDBC) mit Docker  
- Auswerten mit SQL
- Berichten mit BIRT
- Automatisierung pipeline mit ps1

## Tech-Stack
Python, PostgreSQL, Docker, Java/BIRT, …

## Voraussetzungen
- Docker Desktop
- Python 3.12+
- JDBC und BIRT, BIRT-runtime

## Setup

1. Repo klonen
2. `.env` aus `.env.example` erstellen und Passwort setzen
3. Datenbank starten
4. Python-Umgebung anlegen, aktivieren und Pakete installieren
5. Tests ausführen (pytest -v)

## Projektstruktur

```text
job-market-analyse/
├── docs/
│   ├── adr/              # Architekturentscheidungen (ADRs)
│   ├── architecture/     # Pipeline-Diagramm (.drawio + .png)
│   └── notes.md          # Lernnotizen
├── ingestion/            # Schritt 1: Anzeigen über Job-APIs abrufen
├── processing/           # Schritt 3–5: Bereinigen, Extrahieren, Normalisieren
│   └── db.py             # Datenbankverbindung
├── report/               # Schritt 7: Java + BIRT
├── sql/                  # Tabellen und Views
├── tests/                # pytest-Tests
├── .env.example          # Vorlage für Zugangsdaten
├── docker-compose.yml    # PostgreSQL-Container
├── pyproject.toml        # pytest-Konfiguration
├── requirements.txt      # Python-Pakete
└── README.md
```

## Dokumentation
- [Architekturentscheidungen](docs/adr/)
- [Lernnotizen](docs/notes.md)
