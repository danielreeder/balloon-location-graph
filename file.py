import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def get_hour(time):
    return time.hour

def get_time(time):
    return (time.hour*60 + time.minute) / 60

print(pd.read_csv('KK7MXV-11.csv', usecols=["lat", "lng"]).head())
print(pd.read_csv('data_bme280.csv').head())
print(pd.read_csv('data_pms5003.csv').head())
bme = pd.read_csv('data_bme280.csv')
pms = pd.read_csv('data_pms5003.csv')
bme['Time'] = pd.to_datetime(bme['Time'], format='mixed').apply(datetime.time).apply(get_time)
pms['Time'] = pd.to_datetime(pms['Time'], format='mixed').apply(datetime.time).apply(get_time)
print(bme['Time'])
print(pms.columns)
bme.plot.scatter(x='Time', y=' humidity')
bme.plot.scatter(x='Time', y=' pressure')
bme.plot.scatter(x='Time', y=' temperature')
pms.plot.scatter(x='Time', y=[' < 0.3 PM'])
pms.plot.scatter(x='Time', y=[' <0.5 PM'])
pms.plot.scatter(x='Time', y=[' <1.0 PM'])
pms.plot.scatter(x='Time', y=[' <2.5 PM'])
pms.plot.scatter(x='Time', y=[' <10 PM'])

plt.xlabel("Time (hours from midnight)")
plt.show()
