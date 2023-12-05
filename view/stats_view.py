import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

from view.calendar_view import Employee_VEOMSI_View
from view.donut_chart_team_view import DonutChartView

class Stats_view(QTabWidget):
    def __init__(self , db_path):
        super().__init__()
        db_path = db_path

        self.tabTeamDonut = DonutChartView(db_path)
        self.calendarViewOMSI = Employee_VEOMSI_View(db_path)
        
        self.Calendar_VEOMSI_Header = "Visite OMSI"
        self.teamDonutHeader = "Nos equipes"

        self.addTab(self.calendarViewOMSI , self.Calendar_VEOMSI_Header)
        self.addTab(self.tabTeamDonut , self.teamDonutHeader)

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