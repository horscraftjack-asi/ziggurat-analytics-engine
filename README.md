# Ziggurat Analytics Engine — web UI

Hosted front-end for the monthly social data crunch. Upload Meta CSV exports, pick a client,
download the scored performance workbook. No Claude account needed.

## Run locally
    pip install -r requirements.txt
    python app.py
    # open http://localhost:8080

## Deploy (Railway, via GitHub)
Same flow as the YouTube scraper — a second Railway service pointed at a new repo.

1. **Create a new GitHub repo** (e.g. `ziggurat-analytics-engine`) and add these files, keeping
   the folder structure exactly: `app.py` at the root, with `templates/`, `core/`, and `configs/`
   beside it. The structure matters — Flask looks for `templates/` relative to `app.py`, and the
   app imports the engine from `core/`.
2. **In Railway: New Project → Deploy from GitHub repo**, and pick the repo.
3. **Railway auto-detects and builds.** It sees `requirements.txt` (Python), installs the deps,
   reads the `Procfile`, and starts gunicorn. Nothing to configure for the basic deploy. First
   build takes a couple of minutes.
4. **Open the generated URL** — it serves the upload page directly. Pick a client, drop in the
   month's CSVs, download the workbook.

No separate front-end to deploy: the UI ships inside this app (`templates/index.html`) and is
served automatically at the root URL. No build step, no Dockerfile required — the Procfile route
is all Railway needs.

### Required files (all present in this bundle)
- `app.py` — the Flask app (reads `$PORT` from Railway automatically)
- `Procfile` — `web: gunicorn app:app --bind 0.0.0.0:$PORT`
- `requirements.txt` — Python dependencies
- `templates/index.html` — the upload UI
- `core/build_workbook.py` + `core/__init__.py` — the engine (shared with the skill)
- `configs/*.md` — one config per client; the dropdown self-populates from these

## Adding a client
Drop a `[slug]-analytics-config.md` into `configs/` and redeploy — the dropdown self-populates.
Configs are produced by the `analytics-config-intake` skill.

## Architecture
`core/build_workbook.py` is the single source of truth — the SAME file the analytics-engine skill
uses. The web app and the skill both call `run_build()`, so scoring logic never forks.

- Deterministic build (scoring, tabs, formatting): done here, free, instant.
- Written insight tabs (Footnotes/Summary): currently added afterward via the skill. A `/insights`
  endpoint that calls the Claude API is stubbed in `app.py` for a future one-click version.
