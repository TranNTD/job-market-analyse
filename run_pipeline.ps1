# Runs the whole pipeline: 
# 4 Works: Start Database → load data → count skills → create report
# Usage: .\run_pipeline.ps1 [pdf|pptx]

$Python = ".venv\Scripts\python.exe"

Write-Host "1/4 Starting database ..."
docker compose up -d
if ($LASTEXITCODE -ne 0) { Write-Host "Docker failed"; exit 1 }

Write-Host "2/4 Loading CSV files ..."
& $Python -m ingestion.load_csv
if ($LASTEXITCODE -ne 0) { Write-Host "Loading failed"; exit 1 }

Write-Host "3/4 Counting skills ..."
& $Python -m processing.count_skills
if ($LASTEXITCODE -ne 0) { Write-Host "Counting Skills failed"; exit 1}

Write-Host "4/4 Creating report ..."
.\report\run_report.ps1 $args
if ($LASTEXITCODE -ne 0) { Write-Host "Creating report failed"; exit 1}

Write-Host "Done."