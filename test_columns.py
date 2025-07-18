import pandas as pd

# Load your dataset
df = pd.read_csv("data/tweets.csv")

# Print the column names and first few rows
print("=== COLUMN NAMES ===")
print(df.columns)

print("\n=== FIRST 5 ROWS ===")
print(df.head())
