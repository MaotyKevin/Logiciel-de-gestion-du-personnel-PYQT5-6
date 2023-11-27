
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate

from model.calendar_model import Employee_VEOMSI_Model


class Employee_VEOMSI_Controller:
    def __init__(self, db_path):
        self.db_path = db_path
        self.model = Employee_VEOMSI_Model(self.db_path)

    def get_employees_for_date(self , formatted_date):
        return self.model.get_employees_for_date(formatted_date)
    
    def get_all_VE_OMSI_visits(self):
        return self.model.get_all_VE_OMSI_visits()
       



