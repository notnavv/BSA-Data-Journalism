# scrapers/scrape_advanced_stats.py
# Pulls advanced team stats (ORtg, DRtg, NRtg, Pace, SOS, MOV) from Basketball Reference.

import io
import pandas as pd
import cloudscraper
from bs4 import BeautifulSoup

URL = "https://www.basketball-reference.com/leagues/NBA_2026.html"

scraper = cloudscraper.create_scraper()
html = scraper.get(URL, timeout=30).text

soup = BeautifulSoup(html, "lxml")
table = soup.find("table", id="advanced-team")

df = pd.read_html(io.StringIO(str(table)))[0]

# Flatten multi-level column headers
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [b if b and "Unnamed" not in b else a for a, b in df.columns]

# Drop divider rows (where Team is NaN or "Team")
df = df[df["Team"].notna()]
df = df[df["Team"].astype(str).str.lower() != "team"]
df = df[df["Team"].astype(str) != "nan"]

# Keep the columns most useful for modeling
keep = ["Team", "MOV", "SOS", "SRS", "ORtg", "DRtg", "NRtg", "Pace", "TS%"]
df = df[[c for c in keep if c in df.columns]]

for col in df.columns:
    if col != "Team":
        df[col] = pd.to_numeric(df[col], errors="coerce")

df.to_csv("data_raw/advanced_stats.csv", index=False)
print(f"Saved {len(df)} rows to data_raw/advanced_stats.csv")
print(df.head(10))
