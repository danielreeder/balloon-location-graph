import pandas as pd

print(pd.read_csv('KK7MXV-11.csv', usecols=["latitude", "longitude"]).head())