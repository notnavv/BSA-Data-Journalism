# NBA 2025–26 Season: Projected Seedings & Model Findings

## Methodology

Built a linear regression model (R² = 0.942) using six team metrics as predictors of win totals:
Net Rating, Offensive Rating, Defensive Rating, Pace, Strength of Schedule, and Point Differential.
Projected final wins using a blended pace model: 50% full-season win rate + 50% last-15-game win rate,
then adjusted for each team's remaining strength of schedule (harder remaining slate = fewer projected wins).

---

## Projected Final Standings

### Eastern Conference

| Seed | Team                 | Current W | Projected W | Seed Change | L15 Win% |
|------|----------------------|-----------|-------------|-------------|----------|
| 1    | Detroit Pistons      | 45        | 63.3        | —           | 80%      |
| 2    | Boston Celtics       | 41        | 56.0        | —           | 80%      |
| 3    | New York Knicks      | 39        | 53.7        | —           | 73%      |
| 4    | Cleveland Cavaliers  | 38        | 52.1        | —           | 73%      |
| 5    | Toronto Raptors      | 35        | 48.0        | —           | 60%      |
| 6    | Philadelphia 76ers   | 33        | 45.7        | —           | 60%      |
| 7*   | Orlando Magic        | 31        | 43.4        | ↑1          | 53%      |
| 8*   | Miami Heat           | 32        | 43.3        | ↓1          | 53%      |
| 9*   | Charlotte Hornets    | 30        | 43.3        | ↑1          | 80%      |
| 10*  | Atlanta Hawks        | 31        | 42.1        | ↓1          | 60%      |
| 11   | Milwaukee Bucks      | 26        | 36.9        | —           | 53%      |
| 12   | Chicago Bulls        | 25        | 30.6        | —           | 13%      |
| 13   | Washington Wizards   | 16        | 22.3        | —           | 33%      |
| 14   | Brooklyn Nets        | 15        | 20.1        | —           | 20%      |
| 15   | Indiana Pacers       | 15        | 19.9        | —           | 27%      |

*Play-in tournament (seeds 7–10)

### Western Conference

| Seed | Team                       | Current W | Projected W | Seed Change | L15 Win% |
|------|----------------------------|-----------|-------------|-------------|----------|
| 1    | Oklahoma City Thunder      | 47        | 60.7        | —           | 67%      |
| 2    | San Antonio Spurs          | 43        | 59.6        | —           | 80%      |
| 3    | Houston Rockets            | 38        | 52.2        | —           | 67%      |
| 4    | Minnesota Timberwolves     | 38        | 51.8        | —           | 73%      |
| 5    | Los Angeles Lakers         | 36        | 48.4        | ↑1          | 53%      |
| 6    | Denver Nuggets             | 38        | 48.0        | ↓1          | 47%      |
| 7*   | Phoenix Suns               | 34        | 45.5        | —           | 47%      |
| 8*   | Los Angeles Clippers       | 29        | 40.9        | ↑1          | 53%      |
| 9*   | Golden State Warriors      | 31        | 40.5        | ↓1          | 40%      |
| 10*  | Portland Trail Blazers     | 29        | 38.9        | —           | 40%      |
| 11   | Memphis Grizzlies          | 23        | 30.7        | —           | 33%      |
| 12   | New Orleans Pelicans       | 19        | 27.2        | ↑1          | 53%      |
| 13   | Dallas Mavericks           | 21        | 25.8        | ↓1          | 13%      |
| 14   | Utah Jazz                  | 18        | 23.1        | —           | 20%      |
| 15   | Sacramento Kings           | 14        | 18.5        | —           | 13%      |

*Play-in tournament (seeds 7–10)

---

## Key Findings

### Detroit is the season's biggest outlier
The Pistons lead the East at 45 wins and are projected to finish around 63 — but their Net Rating
(+7.9) is actually lower than Boston's (+8.3). They're winning more games than their underlying
metrics suggest they should. Their last-15 win rate is 80%, meaning the hot streak is real right now,
but the gap between their record and their advanced metrics raises a question: are they genuinely
elite, or winning a lot of close games that won't always go their way?

### Charlotte Hornets are the hottest team in the East
The Hornets have the best last-15 win rate in the Eastern Conference at 80%, despite sitting at
just seed 10. The model moves them up one spot in the play-in. Their NRtg (+3.1) is also better
than Orlando's (+0.1) and Atlanta's (0.0), meaning the underlying numbers back up the recent form.

### Denver is fading at exactly the wrong time
The Nuggets are 38-24 and currently hold the 5-seed in the West, but their last-15 win rate is
just 47% and they face the hardest remaining schedule in the West (SOS: 0.550). The model drops
them behind the Lakers to the 6-seed. A first-round matchup with OKC or San Antonio would be
the consequence.

### Dallas is in freefall
The Mavericks have a last-15 win rate of just 13% — the worst in the Western Conference. The
model drops them past New Orleans into the 13-seed and projects them to finish with only ~26 wins.

### The West play-in is a coin flip
The Clippers (↑1) and Warriors (↓1) swap spots based on recent form. LA has won 53% of their
last 15 while Golden State is at 40%. Four games separate the 7-seed Suns from the 10-seed
Trail Blazers — any of those four teams could realistically end up anywhere in that range.

### Regression model fit: R² = 0.942
Net Rating and Point Differential are the two strongest win predictors. Pace has almost no
independent effect once you control for the other variables. The model explains 94.2% of
the variation in win totals across all 30 teams.

---

## Article Thesis

The 2025–26 NBA season has two dominant teams (Detroit, OKC) running away from the field, but
the model shows cracks under Detroit's record that Boston's numbers don't have. In both conferences,
recent form is now more predictive than season-long records — teams like Charlotte, San Antonio,
and the Clippers are trending up, while Denver and Dallas are trending down at exactly the moment
seeding starts to matter most.
