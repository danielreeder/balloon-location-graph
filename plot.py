import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
import seaborn as sns

def main():
    df_steal = pd.read_csv("fire_archive_M6_96619.csv", usecols=["latitude", "longitude", "brightness", "acq_date"], parse_dates=["acq_date"])
    df = pd.read_csv("cfips_location.csv", usecols=["lat", "lng"])
    df['brightness'] = df_steal['brightness']
    df['acq_date'] = df_steal['acq_date']
    df = df.query('lat > 20 and lng < -40')

    # initialize an axis
    fig, ax = plt.subplots(figsize=(8,6))# plot map on axis

    countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

    countries.query("name == 'United States of America' or name == 'Canada'").plot(color="lightgrey",  ax=ax)# parse dates for plot's title

    first_month = df["acq_date"].min().strftime("%b %Y")
    last_month = df["acq_date"].max().strftime("%b %Y")# plot points

    df.plot(x="lng", y="lat", kind="scatter", c="brightness", colormap="YlOrRd", title=f"Fires in Australia {first_month} to {last_month}", ax=ax)# add grid

    ax.grid(alpha=0.5)
    plt.show()

main()
