# models/trajectory_model.py
# Projects final win totals using recent form (last 15 games) + remaining SOS adjustment.

import pandas as pd

games    = pd.read_csv("data_clean/games_clean.csv", parse_dates=["Date"])
teams    = pd.read_csv("data_clean/teams_clean.csv")
schedule = pd.read_csv("data_raw/remaining_schedule.csv")

# ── 1. Per-team game log ────────────────────────────────────────────────────
records = []
for _, row in games.iterrows():
    records.append({"team": row["home_team"], "date": row["Date"], "win": int(row["home_win"]),    "margin": row["margin"]})
    records.append({"team": row["away_team"], "date": row["Date"], "win": int(1 - row["home_win"]), "margin": -row["margin"]})
log = pd.DataFrame(records).sort_values(["team", "date"])

# ── 2. Last-15 win rate per team ────────────────────────────────────────────
recent = (
    log.groupby("team").tail(15)
       .groupby("team")
       .agg(recent_wins=("win","sum"), recent_games=("win","count"))
)
recent["recent_win_pct"] = recent["recent_wins"] / recent["recent_games"]
recent.index.name = "Team"

# ── 3. Remaining SOS ────────────────────────────────────────────────────────
win_pct_map = teams.set_index("Team")["win_pct"]

games_left = (
    pd.concat([schedule["away_team"], schedule["home_team"]])
    .value_counts().rename("games_remaining").rename_axis("Team")
)

def sos_remaining(team):
    opps = pd.concat([
        schedule.loc[schedule["away_team"] == team, "home_team"],
        schedule.loc[schedule["home_team"] == team, "away_team"],
    ])
    return opps.map(win_pct_map).mean()

sos = pd.Series({t: sos_remaining(t) for t in teams["Team"]}, name="sos_remaining")
sos.index.name = "Team"

# ── 4. Projection ───────────────────────────────────────────────────────────
proj = (
    teams.set_index("Team")
    .join(recent[["recent_win_pct"]], how="left")
    .join(sos, how="left")
    .join(games_left, how="left")
)
proj["games_remaining"] = proj["games_remaining"].fillna(0)

# Blended rate: 50% full-season win%, 50% last-15 win%
proj["blended_rate"] = (
    0.50 * proj["win_pct"] +
    0.50 * proj["recent_win_pct"].fillna(proj["win_pct"])
)

# SOS adjustment: harder remaining schedule = fewer projected wins
league_avg_sos = sos.mean()
proj["sos_adj"] = (league_avg_sos - proj["sos_remaining"]) * proj["games_remaining"] * 0.8

proj["projected_wins"] = (
    proj["wins"] + proj["blended_rate"] * proj["games_remaining"] + proj["sos_adj"]
).round(1)

proj = proj.sort_values("projected_wins", ascending=False).reset_index()
proj.to_csv("data_clean/team_features.csv", index=False)

print("=== Projected Final Standings ===\n")
for conf in ["East", "West"]:
    sub = proj[proj["Conference"]==conf].reset_index(drop=True)
    print(f"--- {conf} ---")
    print(sub[["Team","wins","projected_wins","recent_win_pct","sos_remaining"]].to_string(index=False))
    print()
