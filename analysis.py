import pandas as pd

# Load NBA game data
df = pd.read_csv("nba_dailyleaders_full_24_25.csv")

# Calculate average points per game for each player
average_points = df.groupby("Player")["PTS"].mean()

# Rank players from highest to lowest
top_scorers = average_points.sort_values(ascending=False)

# Display the top 10 scorers
print(top_scorers.head(10))
