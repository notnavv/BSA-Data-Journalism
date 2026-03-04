# models/regression_model.py
# Linear regression: which metrics best predict a team's win total?

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

teams = pd.read_csv("data_clean/teams_clean.csv")

# Features: advanced metrics that should predict wins
FEATURES = ["NRtg", "ORtg", "DRtg", "Pace", "SOS", "point_diff"]
TARGET   = "wins"

df = teams[FEATURES + [TARGET, "Team"]].dropna()

X = df[FEATURES]
y = df[TARGET]

model = LinearRegression()
model.fit(X, y)

df = df.copy()
df["predicted_wins"] = model.predict(X).round(1)
df["residual"] = (df["predicted_wins"] - y).round(1)

r2 = r2_score(y, df["predicted_wins"])

print(f"\n=== Regression Results (R² = {r2:.3f}) ===")
print("\nCoefficients (what each metric is worth in wins):")
for feat, coef in sorted(zip(FEATURES, model.coef_), key=lambda x: abs(x[1]), reverse=True):
    print(f"  {feat:15s}  {coef:+.3f}")

print("\n=== Predicted vs Actual Wins ===")
print(df[["Team", "wins", "predicted_wins", "residual"]].sort_values("predicted_wins", ascending=False).to_string(index=False))
