# scrapers/scrape_games.py
# Pulls every completed game for the 2025-26 NBA season from Basketball Reference.

import io
import time
import pandas as pd
import cloudscraper

MONTHS = ["october", "november", "december", "january", "february", "march"]
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

    # Drop repeated header rows and future games (no score yet)
    df = df[df["PTS"] != "PTS"]
    df = df[df["PTS"].notna()]

    all_games.append(df)
    print(f"  {month}: {len(df)} games")
    time.sleep(2.5)  # be polite to BRef

games = pd.concat(all_games, ignore_index=True)

# Keep and rename the columns we care about
games = games[["Date", "Visitor/Neutral", "PTS", "Home/Neutral", "PTS.1"]].rename(columns={
    "Visitor/Neutral": "away_team",
    "PTS":             "away_score",
    "Home/Neutral":    "home_team",
    "PTS.1":           "home_score",
})

games["away_score"] = pd.to_numeric(games["away_score"])
games["home_score"] = pd.to_numeric(games["home_score"])

games.to_csv("data_raw/games.csv", index=False)
print(f"\nSaved {len(games)} games to data_raw/games.csv")
print(games.head())
