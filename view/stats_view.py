import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

from view.calendar_view import Employee_VEOMSI_View
from view.donut_chart_team_view import DonutChartView
from view.donut_chart_category_view import DonutChartViewCategory
from view.donut_chart_SC_view import DonutChartViewSC

class Stats_view(QTabWidget):
    def __init__(self , db_path):
        super().__init__()
        db_path = db_path

        self.tabTeamDonut = DonutChartView(db_path)
        self.calendarViewOMSI = Employee_VEOMSI_View(db_path)
        self.tabCategoryDonut = DonutChartViewCategory(db_path)
        self.tabSCDonut = DonutChartViewSC(db_path)
        
        self.Calendar_VEOMSI_Header = "Visite OMSI"
        self.teamDonutHeader = "Nos equipes"
        self.categoryHeader = "Categories"
        self.SCHeader = "Sous-categorie"

        self.addTab(self.calendarViewOMSI , self.Calendar_VEOMSI_Header)
        self.addTab(self.tabTeamDonut , self.teamDonutHeader)
        self.addTab(self.tabCategoryDonut , self.categoryHeader)
        self.addTab(self.tabSCDonut , self.SCHeader)

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