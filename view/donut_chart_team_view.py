import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Circle
from PyQt5.QtCore import QTimer

import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from controller.stats_controller import Stats_controller

class DonutChartView(QWidget):
    def __init__(self , db_path):
        super().__init__()
        
        self.db_path = db_path
        self.controller = Stats_controller(self.db_path)

        self.figure, self.ax = Figure(), None
        self.canvas = FigureCanvas(self.figure)

        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(3000) 

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        self.update_chart()

    def update_chart(self):
        data = self.controller.display_donut_chart_team()
        labels = [team[0] for team in data]
        sizes = [team[1] for team in data]

        if self.ax is not None:
            self.ax.clear()

        self.ax = self.figure.add_subplot(111)
        self.ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        center_circle = Circle((0, 0), 0.70, fc='white')  # Use Circle from matplotlib.patches
        self.ax.add_patch(center_circle)
        self.ax.axis('equal')

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = DonutChartView("data\my_database.sqlite")
    view.show()
    sys.exit(app.exec_())
