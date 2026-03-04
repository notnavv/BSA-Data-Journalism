# scrapers/scrape_schedule.py
# Pulls remaining (unplayed) games for the 2025-26 NBA season from Basketball Reference.

import io
import time
import pandas as pd
import cloudscraper

MONTHS = ["march", "april"]  # adjust if season extends further
BASE_URL = "https://www.basketball-reference.com/leagues/NBA_2026_games-{month}.html"

scraper = cloudscraper.create_scraper()
all_games = []

for month in MONTHS:
    url = BASE_URL.format(month=month)
    r = scraper.get(url, timeout=30)

    if r.status_code != 200:
        print(f"Skipping {month} (status {r.status_code})")
        continue

    df = pd.read_html(io.StringIO(r.text))[0]

    # Drop repeated header rows
    df = df[df["PTS"] != "PTS"]

    # Keep only future games (no score yet)
    df = df[df["PTS"].isna()]

    if len(df) == 0:
        print(f"  {month}: no remaining games")
        continue

    all_games.append(df)
    print(f"  {month}: {len(df)} remaining games")
    time.sleep(2.5)

if not all_games:
    print("No remaining games found.")
else:
    schedule = pd.concat(all_games, ignore_index=True)

    schedule = schedule[["Date", "Visitor/Neutral", "Home/Neutral"]].rename(columns={
        "Visitor/Neutral": "away_team",
        "Home/Neutral":    "home_team",
    })

    schedule.to_csv("data_raw/remaining_schedule.csv", index=False)
    print(f"\nSaved {len(schedule)} remaining games to data_raw/remaining_schedule.csv")
    print(schedule.head())
