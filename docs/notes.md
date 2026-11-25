# Docker
docker compose up -d : Create Volume, Network, and Container
docker compose ps : check status of docker
docker compose down: remove Container, Network
docker compose down -v: remove Container, Network and Volume (completely delete)
docker compose stop while pytest: test_db_connection cannot passed
docker compose start: pytest works perfect

## Downside of Docker
Docker and the database then always run in the background and use memory, even on days when you're not working on the project. (if start automatically)
Make a backup, especially before bigger changes:
    docker exec ba_jobs_db pg_dump -U ba_user ba_jobs > backups\ba_jobs_2026-11-24.sql

Free upu Disk space. Docker collects old, unused images over time:
    docker system df          # how much space Docker uses
    docker image prune        # removes unused images (your volume stays untouched)

## routine with docker
Start Docker Desktop, if it isn't running yet. Wait until it shows Engine running (green).
In the project folder:
    docker compose up -d
    docker compose ps          # wait for "healthy"
Ending a work session
    docker compose stop         # This pauses the database and frees memory and CPU. The data stays.

# SQL
ON DELETE CASCADE: if delete one, the dependencies will also be deleted
ALTER TABLE table_name ALTER COLUMN column_name DROP NOT NULL
Get-Content sql\001_schema.sql | docker exec -i container_name psql -U POSTGRES_USER -d POSTGRES_DB

md5: hash function - turns any text, however long, into a short fingerprint of 32 characters.
=> shorter and faster if we have big data base and long description text. 
ILIKE: Like LIKE, but ignores upper/lower case. % stands for any text, so this matches "Senior Business Analyst", "Business Analysis" and so on.

# Pytest
unit tests  - test local data-cases without db
integration tests - test data cases on db
conftest.py - support intergration tests with db_conn
terminal: pytest -v
pytest.mark.parametrize

# Git
## Tag
git tag                          # list all tags
git show v0.2.0                  # show the tag message and the commit
git tag -d v0.2.0                # delete a tag locally (e.g. if it was set on the wrong commit)
git push origin --delete v0.2.0  # also delete it on GitHub

A tag is a readable name that permanently points to one specific commit:
main:  ●───●───●───●───●───●   ← main keeps moving with new commits
                   │       │
               v0.1.0   v0.2.0  ← tags stay where they were set
           (Phase 0 done) (MVP: first PDF)
Advantages: 
    - Go back to a version: git switch --detach v0.2.0 shows the project exactly as it was at the MVP. (git switch main brings you back.)
    - Compare versions: git diff v0.1.0 v0.2.0 --stat shows everything that changed between Phase 0 and the MVP.
    - Show progress: In job applications, a list of versions shows how the project grew step by step.

What the version number means: Semantic Versioning
    v 0 . 2 . 0
  │   │   └── PATCH: small fixes
  │   └────── MINOR: new features
  └────────── MAJOR: big, incompatible changes

# BIRT
Cannot show Bar-chart in Preview but work with export (in PDF)

# run_report.ps1
use birt birt-runtime\ReportEngine to export pdf-report