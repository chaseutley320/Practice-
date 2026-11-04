# Thunder Lab

An interactive Oklahoma City Thunder performance dashboard by Chase Utley, analyzing the 2024–25 regular season.

## Project question
How did Oklahoma City's scoring margin and consistency vary over the season, and how did production differ across its rotation?

## Features
- 82 real regular-season games with month and home/away filters
- Recomputed win rate, points scored, points allowed, and scoring margin
- Game-by-game SVG charts and monthly margin comparisons
- 12-player leaderboard, searchable statistics, and head-to-head comparison
- CSV downloads and documented sources
- Responsive HTML/CSS and vanilla JavaScript; Python data preparation; no API keys

This project lives in `thunder-lab/` alongside the original NBA scoring analysis and uses its own documented snapshot.

## Run locally
```sh
cd thunder-lab
python3 -m http.server 8000 --directory dist
```
Open http://localhost:8000. Use a server rather than opening index.html directly because the app fetches data.json.

## Reproduce and validate data
```sh
python3 build_data.py
python3 validate.py
node --check dist/app.js
```
The Python preparation script transforms a checked-in, manually transcribed snapshot into JSON and CSV. It is not an automated scraper or live API pipeline.

## Data provenance
Retrieved November 3, 2026:
- https://hoopsavant.com/stats/teams/thunder/2024-25 — game results and player per-game averages
- https://www.basketball-reference.com/teams/OKC/2025.html — team aggregate cross-check
- https://champsorchumps.us/team/nba/oklahoma-city-thunder/2025 — game score cross-check

The December 14 semifinal is classified as Neutral, verified at https://www.nba.com/game/HOU-vs-OKC-0022401230/box-score. There are 41 home, 40 away and one neutral-site game. Regular season only; excludes playoffs and the NBA Cup final. The 12 selected players are a rotation subset, not the complete roster. Per-game player averages are rounded by the source, so multiplying them by games does not produce exact season totals.

## Methodology
Win rate = wins / games. PPG = sum(points) / games. Opponent PPG = sum(allowed) / games. Margin = sum(points - allowed) / games. Team filters apply to KPI cards, trend chart, and game log. Monthly bars apply only the venue filter, with the selected month highlighted. Result filter applies only to the game log. Players remain full-season throughout.

A 68–14 record corresponds to an 82.9% win rate. The team averaged 120.5 points scored and 107.6 allowed, a +12.9 margin. These are descriptive results, not estimates of individual causal impact. Player roles, minutes and availability differ.

## Hosting
A private hosted preview is available to the project owner. To deploy publicly on GitHub Pages, configure the repository to serve this project's dist/ directory through a Pages workflow.

## Structure
- dist/ — deployable app, JSON, CSV
- build_data.py — reproducible snapshot preparation
- validate.py — data integrity checks

## Resume wording
Use after reviewing and understanding the implementation:
“Developed an interactive NBA analytics dashboard using Python and JavaScript to analyze 82 games and compare 12 players, with dynamic filters, data validation, and documented metrics.”

## Limitations
Historical snapshot, not live statistics. No shot tracking, lineup-level impact, forecasting, or possession-adjusted efficiency. Independent portfolio project; not affiliated with the NBA or Oklahoma City Thunder.
