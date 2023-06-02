import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
import seaborn as sns

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
        self.layout_temp = QVBoxLayout()
        
        self.sc = MplCanvas(self, width=50, height=30, dpi=100)
        # self.sc_temp = MplCanvas(self, width=50, height=30, dpi=100)
        df_kk7 = pd.read_csv('KK7MXV-11.csv')
        df_ko4 = pd.read_csv('KO4TL-11.csv')
        # df_kk7['temp'] = df_kk7[['comment']].apply(self.parse_comment, axis=1)
        # df_ko4['temp'] = df_ko4[['comment']].apply(self.parse_comment, axis=1)
        # print("ko4:" + df_ko4['temp'])
        states = gpd.read_file('data/usa-states-census-2014.shp')
        states.query("NAME == 'Oregon'").boundary.plot(color='black', ax=self.sc.ax)  
        roads = gpd.read_file('data/USA_roads.shp')
        roads.plot(color='black', ax=self.sc.ax)
        self.sc.ax.scatter(x=df_kk7['lng'], y=df_kk7['lat'], c=df_kk7['altitude'], cmap='Blues', s=10)
        self.sc.ax.scatter(x=df_ko4['lng'], y=df_ko4['lat'], c=df_ko4['altitude'], cmap='Reds', s=10)
        self.sc.ax.grid(alpha=0)
        self.sc.ax.set_xlabel('Longitude')
        self.sc.ax.set_ylabel('Latitude')
        self.sc.ax.set_xlim(min(min(df_kk7['lng']), min(df_ko4['lng']))-.05, max(max(df_kk7['lng']), max(df_ko4['lng']))+.05)
        self.sc.ax.set_ylim(min(min(df_kk7['lat']), min(df_ko4['lat']))-.05, max(max(df_kk7['lat']), max(df_ko4['lat']))+.05)
        # self.sc_temp.ax.scatter(x=df_kk7['lng'], y=df_kk7['lat'], c=df_kk7['temp'], cmap='plasma', s=10)
        # self.sc_temp.ax.scatter(x=df_ko4['lng'], y=df_ko4['lat'], c=df_ko4['temp'], cmap='plasma', s=10)
        # self.sc_temp.ax.grid(alpha=0)
        # self.sc_temp.ax.set_xlabel('Longitude')
        # self.sc_temp.ax.set_ylabel('Latitude')
        # self.sc_temp.ax.set_xlim(min(min(df_kk7['lng']), min(df_ko4['lng']))-.05, max(max(df_kk7['lng']), max(df_ko4['lng']))+.05)
        # self.sc_temp.ax.set_ylim(min(min(df_kk7['lat']), min(df_ko4['lat']))-.05, max(max(df_kk7['lat']), max(df_ko4['lat']))+.05)
        submit = QPushButton('Swap')
        submit.clicked.connect(self.update_plot)
        self.j = 0
        
        self.signal.connect(self.update_plot)
        self.layout.addWidget(submit)
        self.layout.addWidget(self.sc)
        # self.layout_temp.addWidget(self.c.sc_temp)
        
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.show()
        
    def update_plot(self):
        if j%2 == 0:
            self.widget.setLayout(self.layout_temp)
            j += 1
            return
        self.widget.setLayout(self.layout)

    def parse_comment(self, comment):
        print(comment[0])
        return comment[0].split(' ')[1]

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
    print('hello world!')
        

    
    
if __name__ == '__main__':
    main()