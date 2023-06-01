import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
import seaborn as sns

# def main():
#     df_steal = pd.read_csv("fire_archive_M6_96619.csv", usecols=["latitude", "longitude", "brightness", "acq_date"], parse_dates=["acq_date"])
#     df = pd.read_csv("cfips_location.csv", usecols=["lat", "lng"])
#     df['brightness'] = df_steal['brightness']
#     df['acq_date'] = df_steal['acq_date']
#     df = df.query('lat > 20 and lng < -40')

#     # initialize an axis
#     fig, ax = plt.subplots(figsize=(8,6))# plot map on axis

#     countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

#     countries.query("name == 'United States of America' or name == 'Canada'").plot(color="lightgrey",  ax=ax)# parse dates for plot's title    
#     first_month = df["acq_date"].min().strftime("%b %Y")
#     last_month = df["acq_date"].max().strftime("%b %Y")# plot points

#     df.plot(x="lng", y="lat", kind="scatter", c="brightness", colormap="YlOrRd", title=f"Fires in Australia {first_month} to {last_month}", ax=ax)# add grid

#     ax.grid(alpha=0.5)
#     plt.show()
from cmath import nan
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5 import QtWidgets, QtCore
import sys
from time import sleep



from email.charset import QP
import sys
import matplotlib
import numpy as np
import pandas as pd
matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    signal = QtCore.pyqtSignal(int)
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.init_ui()

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.

    def init_ui(self):
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        
        self.sc = MplCanvas(self, width=50, height=30, dpi=100)
        df_steal = pd.read_csv("fire_archive_M6_96619.csv", usecols=["latitude", "longitude", "brightness", "acq_date"], parse_dates=["acq_date"])
        df = pd.read_csv('/Users/danielreeder/Downloads/geopandas-tutorial-master/data/uscities.csv', usecols=['state_name', 'lat', 'lng']).query("state_name == 'Oregon'").reset_index()

        self.lng = df['lng']
        self.lat = df['lat']
        df['brightness'] = df_steal['brightness']
        states = gpd.read_file('/Users/danielreeder/Downloads/geopandas-tutorial-master/data/usa-states-census-2014.shp')
        states.query("NAME == 'Oregon'").boundary.plot(color='black', ax=self.sc.ax)  
        states.query("NAME == 'Oregon'").plot(ax=self.sc.ax) 
        self.bright = df['brightness']
        self.to_plot_lng = np.array(self.lng[0])
        self.to_plot_lat = np.array(self.lat[0])
        self.to_plot_bright = np.array(self.bright[0])
        self.sc.ax.scatter(x=self.to_plot_lng, y=self.to_plot_lat, c=self.to_plot_bright, cmap='Blues')
        self.sc.ax.grid(alpha=0)
        self.sc.ax.set_xlabel('Longitude')
        self.sc.ax.set_ylabel('Latitude')
        submit = QPushButton('Refresh')
        submit.clicked.connect(self.update_plot)
        self.j = 0
        
        self.signal.connect(self.update_plot)
        self.layout.addWidget(submit)
        self.layout.addWidget(self.sc)
        
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.show()
        
    def update_plot(self):
        self.to_plot_lng = np.append(self.to_plot_lng, self.lng[self.j])
        self.to_plot_lat = np.append(self.to_plot_lat, self.lat[self.j])
        self.to_plot_bright = np.append(self.to_plot_bright, self.bright[self.j])
        self.sc.ax.scatter(x=self.to_plot_lng, y=self.to_plot_lat, c=self.to_plot_bright, cmap='Blues')
        self.sc.ax.set_xlabel('Longitude')
        self.sc.ax.set_ylabel('Latitude')
        self.sc.draw_idle() 
        self.j += 1

    def clicked(self):
        self.to_plot_lng = np.append(self.to_plot_lng, self.lng[self.j])
        self.to_plot_lat = np.append(self.to_plot_lat, self.lat[self.j])
        self.to_plot_bright = np.append(self.to_plot_bright, self.bright[self.j])
        self.sc.ax.scatter(x=self.to_plot_lng, y=self.to_plot_lat, c=self.to_plot_bright, cmap='Blues')
        self.sc.ax.set_xlabel('Longitude')
        self.sc.ax.set_ylabel('Latitude')
        self.sc.draw_idle() 
        self.j += 1
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
    print('hello world!')
        

    
    
if __name__ == '__main__':
    main()