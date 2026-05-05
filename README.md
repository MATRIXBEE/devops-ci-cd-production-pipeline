# DevOps CI/CD Production Pipeline (Flask)

## Project Overview

This repository provides a production-style baseline for containerized Python service delivery with automated CI checks.  
It includes a Flask API, Pytest test suite, Docker packaging, and a GitHub Actions pipeline that validates application quality on every push to `main`.

## Features

- Structured Flask application with factory pattern
- REST API endpoints for service status and health checks
- Centralized, basic application logging
- Automated endpoint testing with Pytest
- Docker image build for consistent runtime packaging
- GitHub Actions workflow for CI test-and-build validation
- Compose definition for local container orchestration

## Tech Stack

- Python 3.12
- Flask
- Pytest
- Docker / Docker Compose
- GitHub Actions

## Repository Structure

```text
.
|-- .github/
|   `-- workflows/
|       `-- ci.yml
|-- app/
|   |-- __init__.py
|   |-- config.py
|   |-- main.py
|   `-- routes.py
|-- tests/
|   |-- conftest.py
|   `-- test_endpoints.py
|-- .gitignore
|-- Dockerfile
|-- docker-compose.yml
|-- README.md
`-- requirements.txt
```

## API Endpoints

- `GET /` -> `Service is running`
- `GET /health` -> `{"status":"ok"}`

## Run Locally

### Option 1: Local Python runtime

1. Create virtual environment and activate it:
   - Windows (PowerShell): `python -m venv .venv; .\.venv\Scripts\Activate.ps1`
   - Linux/macOS: `python -m venv .venv && source .venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Start the service: `python -m app.main`
4. Verify:
   - `http://localhost:5000/`
   - `http://localhost:5000/health`

### Option 2: Docker Compose

1. Build and run: `docker compose up --build`
2. Verify:
   - `http://localhost:5000/`
   - `http://localhost:5000/health`
3. Stop services: `docker compose down`

## Running Tests

Run the suite with:

```bash
pytest -q
```

## CI/CD Workflow

The workflow is defined at `.github/workflows/ci.yml` and runs on push to `main`.

Pipeline stages:

1. Checkout repository source
2. Setup Python 3.12
3. Install dependencies from `requirements.txt`
4. Execute Pytest test suite
5. Build Docker image tagged with commit SHA

This ensures every change merged to `main` is validated for application correctness and container build integrity.
