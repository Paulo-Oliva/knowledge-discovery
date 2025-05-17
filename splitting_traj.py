import pandas as pd

df = pd.read_parquet("data/trajectories.parquet")

# Group by month and save each to a separate Parquet file
for (year, month), group in df.groupby([df["TIMESTAMP"].dt.year, df["TIMESTAMP"].dt.month]):
    sample = group.sample(frac=0.01, random_state=42)
    filename = f"data/monthly/trajectory_samples/trips_{year}_{month:02d}.parquet"
    sample.to_parquet(filename)
    print(f"Saved {len(sample)} rows to {filename}")
