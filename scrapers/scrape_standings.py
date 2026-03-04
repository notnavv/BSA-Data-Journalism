# scrapers/scrape_standings.py

import io
import pandas as pd
import cloudscraper

URL = "https://www.basketball-reference.com/leagues/NBA_2026_standings.html"

scraper = cloudscraper.create_scraper()
html = scraper.get(URL, timeout=30).text

tables = pd.read_html(io.StringIO(html))
east = tables[0].rename(columns={tables[0].columns[0]: "Team"})
west = tables[1].rename(columns={tables[1].columns[0]: "Team"})

east["Conference"] = "East"
west["Conference"] = "West"

standings = pd.concat([east, west], ignore_index=True)
standings["Team"] = standings["Team"].str.replace(r"\s*\(\d+\)", "", regex=True).str.strip()
standings = standings[standings["Team"].str.lower() != "team"].reset_index(drop=True)

standings.to_csv("data_raw/standings.csv", index=False)
print(standings.head(10))
