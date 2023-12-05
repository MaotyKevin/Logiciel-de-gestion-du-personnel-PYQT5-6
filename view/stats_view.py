import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

from view.donut_chart_team_view import DonutChartView

class Stats_view(QTabWidget):
    def __init__(self , db_path):
        super().__init__()
        db_path = db_path

        tabTeamDonut = DonutChartView(db_path)

        self.teamDonutHeader = "Nos equipes"

        self.addTab(tabTeamDonut , self.teamDonutHeader)

        self.setStyleSheet(
            "QTabBar::tab {"
            "    font-weight: bold;"
            "    width: 150px;"
            "}"
            "QTabBar::tab:!selected {"
            "    background-color: #7ed957;"
            "    color: #102429;   "
            "}"
        )