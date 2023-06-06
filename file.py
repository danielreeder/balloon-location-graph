import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# return the time in hours given a time  in hours and minutes
def get_time(time): return (time.hour*60 + time.minute) / 60

# read in the data from the bme280 and pms5003 and store them as DataFrames
bme = pd.read_csv('data_bme280.csv')
pms = pd.read_csv('data_pms5003.csv')

# apply the get_time function to the time column in order to make it a usable value
bme['Time'] = pd.to_datetime(bme['Time'], format='mixed').apply(datetime.time).apply(get_time)
pms['Time'] = pd.to_datetime(pms['Time'], format='mixed').apply(datetime.time).apply(get_time)

# plot and save graphs of each different measurement over time
bme.plot.scatter(x='Time', y=' humidity', s=5, title='Humidity vs. Time')
plt.xlabel("Time (hours from midnight)")
plt.savefig('C:/Users/danie/Desktop/hum.png')
bme.plot.scatter(x='Time', y=' pressure', s=5, title='Pressure vs. Time')
plt.xlabel("Time (hours from midnight)")
plt.savefig('C:/Users/danie/Desktop/pre.png')
bme.plot.scatter(x='Time', y=' temperature', s=5, title='Temperature vs. Time')
plt.xlabel("Time (hours from midnight)")
plt.savefig('C:/Users/danie/Desktop/tem.png')
ax = pms.plot.scatter(x='Time', y=[' < 0.3 PM'], color='black', label='<0.3 PM', s=5, title='Particulate Matter vs. Time')
pms.plot.scatter(x='Time', y=[' <0.5 PM'], color='r', label='<0.5 PM', ax=ax, s=5)
pms.plot.scatter(x='Time', y=[' <1.0 PM'], color='g', label='<1.0 PM', ax=ax, s=5)
pms.plot.scatter(x='Time', y=[' <2.5 PM'], color='b', label='<2.5 PM', ax=ax, s=5)
pms.plot.scatter(x='Time', y=[' <10 PM'], color='purple', label='<10 PM', ax=ax, s=5, ylabel='PM Concentration')
plt.savefig('C:/Users/danie/Desktop/pm.png')
plt.xlabel("Time (hours from midnight)")
plt.show()
