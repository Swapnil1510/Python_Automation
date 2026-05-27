# requirements.txt — Dependencies & Setup

This project uses `requirements.txt` to pin Python dependencies required for testing, API and browser automation.

## Prerequisites
- Python 3.8 or newer
- `pip` (bundled with recent Python)
- Optional: Git (for cloning repository)

## Quick setup
1. Create and activate a virtual environment:

   - PowerShell (Windows):

     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

   - Command Prompt (Windows):

     ```cmd
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - macOS / Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install Playwright browsers (required if `playwright` is used):

```bash
python -m playwright install
```

## Running tests (examples)
- Run all tests with pytest:

```bash
pytest
```

- Generate Allure results (if using Allure):

```bash
pytest --alluredir=allure-results
```

## Update `requirements.txt`
After adding or upgrading packages in your environment, update the lock file:

```bash
pip freeze > requirements.txt
```

## Packages included
The current `requirements.txt` contains the following packages (grouped by purpose):

- Testing and test utilities: pytest, pytest-cov, pytest-mock, pytest-asyncio, pytest-cases, pytest-xdist, pytest-bdd, pytest-benchmark, pytest-html
- Browser automation: playwright
- Reporting: allure-pytest
- Data handling: pydantic, python-dotenv, openpyxl, pandas, PyPDF2
- SSH / file transfer: paramiko
- HTTP client: requests
- gRPC / Protobuf: grpcio, protobuf, grpcio-tools, grpcio-reflection
- Database connector: psycopg2-binary

## Notes
- Prefer working inside a virtual environment to avoid polluting global Python packages.
- `psycopg2-binary` may require additional system libraries on some platforms; if you encounter installation errors, consult its docs for platform-specific prerequisites.
- If CI or Docker is used, install dependencies in the environment created by that pipeline instead of the local venv.

If you'd like, I can also add example `pytest` and `playwright` commands to `Makefile` or a small `scripts/` folder for convenience.
