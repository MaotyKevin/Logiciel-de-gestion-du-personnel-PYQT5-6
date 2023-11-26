import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
import sqlite3

import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from model.calendar_model import Employee_VEOMSI_Model
from controller.calendar_controller import Employee_VEOMSI_Controller

class Employee_VEOMSI_View(QWidget):
    def __init__(self , db_path):
        super().__init__()
        self.db_path = db_path
        self.controller = Employee_VEOMSI_Controller(self.db_path)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Employee Calendar App')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout(self)

        # Calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setSelectedDate(QDate.currentDate())
        layout.addWidget(self.calendar)
        self.calendar.setStyleSheet("""
            QCalendarWidget QWidget {
                background-color: #102429;
                alternate-background-color: black;
                color:white;
            }
        """)

        # Employee list table
        self.employee_table = QTableWidget(self)
        self.employee_table.setColumnCount(6)
        self.employee_table.setHorizontalHeaderLabels(['Badge', 'Nom' , 'Prenoms' , 'CIN' , 'Fonction' , 'Categorie'])
        layout.addWidget(self.employee_table)

        # Connect signals to slots
        self.calendar.clicked.connect(self.update_employee_list)
        self.update_employee_list()  # Initial update based on the current date

    def update_employee_list(self):
        selected_date = self.calendar.selectedDate()

        formatted_date = selected_date.toString("ddd MMM dd yyyy")
        print(formatted_date)
        employees = self.controller.get_employees_for_date(formatted_date)

        self.populate_employee_table(employees)

    def populate_employee_table(self, employees):
        self.employee_table.setRowCount(0)  # Clear existing rows

        for row, employee in enumerate(employees):
            self.employee_table.insertRow(row)
            for col, value in enumerate(employee):
                item = QTableWidgetItem(str(value))
                item.setFlags(Qt.ItemIsEnabled)  # Make cells read-only
                self.employee_table.setItem(row, col, item)





if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = Employee_VEOMSI_Model("data\my_database.sqlite")
    view = Employee_VEOMSI_View()
    controller = Employee_VEOMSI_Controller(model, view)

    view.show()

    sys.exit(app.exec_())

    #date = "sam. nov. 25 2023"
    #result = model.get_employees_for_date(date)
    #for results in result:
    #    print(results)


