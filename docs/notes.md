# Docker
docker compose up -d : Create Volume, Network, and Container
docker compose ps : check status of docker
docker compose down: remove Container, Network
docker compose down -v: remove Container, Network and Volume
docker compose stop while pytest: test_db_connection cannot passed
docker compose start: pytest works perfect

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