import matplotlib
import numpy as np
import pandas as pd
import geopandas as gpd

def parse_comment(comment):
    return comment[0].split(' ')[1]

df_kk7 = pd.read_csv('C:/Users/dreeder.AD.003/Downloads/KK7MXV-11.csv')
df_ko4 = pd.read_csv('C:/Users/dreeder.AD.003/Downloads/KO4TL-11.csv')
df_kk7['temp'] = df_kk7[['comment']].apply(parse_comment, axis=1).apply(str.strip, args='C')
df_ko4['temp'] = df_ko4[['comment']].apply(parse_comment, axis=1).apply(str.strip, args='C')
df_kk7['temp'][0] = 0
df_ko4['temp'][0] = 0
states = gpd.read_file('data/usa-states-census-2014.shp')
oregon = states.query("NAME == 'Oregon'").boundary.plot(color='black')  
roads = gpd.read_file('data/USA_roads.shp')
roads.plot(color='black', ax=oregon)
df_kk7.plot.scatter(x='lng', y='lat', color=df_kk7['altitude'], cmap='Blues', s=10, ax=oregon)
# self.sc.ax.scatter(x=df_ko4['lng'], y=df_ko4['lat'], c=df_ko4['altitude'], cmap='Reds', s=10)
# self.sc.ax.grid(alpha=0)
# self.sc.ax.set_xlabel('Longitude')
# self.sc.ax.set_ylabel('Latitude')
# self.sc.ax.set_xlim(min(min(df_kk7['lng']), min(df_ko4['lng']))-.05, max(max(df_kk7['lng']), max(df_ko4['lng']))+.05)
# self.sc.ax.set_ylim(min(min(df_kk7['lat']), min(df_ko4['lat']))-.05, max(max(df_kk7['lat']), max(df_ko4['lat']))+.05)
# self.sc_temp.ax.scatter(x=df_kk7['lng'], y=df_kk7['lat'], c=df_kk7['temp'], cmap='Blues', s=10)
# self.sc_temp.ax.scatter(x=df_ko4['lng'], y=df_ko4['lat'], c=df_ko4['temp'], cmap='plasma', s=10)
# self.sc_temp.ax.grid(alpha=0)
# self.sc_temp.ax.set_xlabel('Longitude')
# self.sc_temp.ax.set_ylabel('Latitude')
# self.sc_temp.ax.set_xlim(min(min(df_kk7['lng']), min(df_ko4['lng']))-.05, max(max(df_kk7['lng']), max(df_ko4['lng']))+.05)
# self.sc_temp.ax.set_ylim(min(min(df_kk7['lat']), min(df_ko4['lat']))-.05, max(max(df_kk7['lat']), max(df_ko4['lat']))+.05)
# submit = QPushButton('Swap')
# submit.clicked.connect(self.update_plot)
# self.j = 0

# self.signal.connect(self.update_plot)
# self.layout.addWidget(submit)
# # self.layout.addWidget(self.sc)
# self.layout_temp.addWidget(self.sc_temp)

# # self.widget.setLayout(self.layout)
# self.widget.setLayout(self.layout_temp)
# self.setCentralWidget(self.widget)
# self.show()

