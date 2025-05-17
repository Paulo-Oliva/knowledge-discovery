# This short script explodes (splits) the lists of coordinates and timestamps in the `df` dataframe into separate rows.
# This is useful for visualizing the data in a map more easily.

import pandas as pd

df = pd.read_parquet("data/train_cleaned.parquet")

df = df.drop(columns=["POLYLINE", "START", "END", "ORIGIN_CALL", "ORIGIN_STAND"])

df = df.explode(["LONGITUDE", "LATITUDE", "TIMESTAMP"])

df.to_parquet("data/trajectories.parquet")
