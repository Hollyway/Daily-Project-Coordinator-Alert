# Ontario Project Coordinator & Canada Remote Alert Bot

Standalone GitHub Actions bot for:

- all Project Coordinator-type roles in Ontario (onsite, hybrid, or remote)
- remote roles anywhere in Canada
- adjacent PMO / implementation / delivery / project analyst roles

## Files

- `main.py` — orchestrates the run
- `scraper/` — LinkedIn, Workday, and Canada Job Bank scrapers
- `filter.py` — keeps Ontario coordinator roles and Canada remote roles only
- `deduplicator.py` — stores previously emailed jobs in `seen_jobs_project_coord.json`
- `.github/workflows/daily_project_coordinator_alert.yml` — scheduled workflow

## Setup

1. Create a new GitHub repo
2. Upload all files in this folder
3. Add a repository secret named `GMAIL_APP_PASSWORD`
4. Make sure `SENDER_EMAIL` in `config.py` matches the Gmail account used to create the app password
5. Run the workflow once from the Actions tab
