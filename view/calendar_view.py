import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QTableWidget, QTableWidgetItem , QScrollArea , QSizePolicy , QHeaderView
from PyQt5.QtCore import Qt, QDate 
from PyQt5.QtGui import QTextCharFormat , QColor
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

        scroll_area = QScrollArea(self)
        layout.addWidget(scroll_area)

        scroll_area.setStyleSheet(
            """
            QScrollArea {
                border: 1px solid #CCCCCC;
            }
            
            QScrollBar:vertical {
                border: 1px solid white;
                background: #102429;
                width: 12px;
                margin: 0px;
            }
            
            QScrollBar:horizontal {
                border: 1px solid white;
                background: #102429;
                height: 12px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #102429;
                min-height: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::handle:horizontal {
                background: #102429;
                min-width: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
            }
            """
        )

        # Employee list table
        self.employee_table = QTableWidget(self)
        self.employee_table.setColumnCount(7)
        self.employee_table.setHorizontalHeaderLabels(['Badge', 'Nom' , 'Prenoms' , 'CIN' , 'DU', 'Fonction' , 'Categorie'])

        header_style = """
            QHeaderView::section {
                background-color: #102429;
                color: white;
                padding: 4px;
                border: 1px solid #7ed957;
                border-radius: 0px;
                font-weight:bold;
            }
        """
        self.employee_table.horizontalHeader().setStyleSheet(header_style)

        scroll_area.setWidget(self.employee_table)
        scroll_area.setWidgetResizable(True)

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Disable horizontal scrollbar
        scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.employee_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        # Connect signals to slots
        self.calendar.clicked.connect(self.update_employee_list)
        self.update_employee_list()  # Initial update based on the current date

    def update_employee_list(self):
        selected_date = self.calendar.selectedDate()

        formatted_date = selected_date.toString("ddd MMM dd yyyy")
        print(formatted_date)
        employees = self.controller.get_employees_for_date(formatted_date)

        self.populate_employee_table(employees)
        self.highlight_dates_with_data()

    def populate_employee_table(self, employees):
        self.employee_table.setRowCount(0)  # Clear existing rows

        for row, employee in enumerate(employees):
            self.employee_table.insertRow(row)
            for col, value in enumerate(employee):
                item = QTableWidgetItem(str(value))
                item.setFlags(Qt.ItemIsEnabled)  # Make cells read-only
                self.employee_table.setItem(row, col, item)

    def highlight_dates_with_data(self):
        highlighted_format = QTextCharFormat()
        highlighted_format.setBackground(QColor("#7ed957"))  # Green background color
        

        all_visits = self.controller.get_all_VE_OMSI_visits()

        for visit_date in all_visits:
            date = QDate.fromString(visit_date, "ddd MMM dd yyyy")  # Adjust the date format

            if not date.isNull():
                self.calendar.setDateTextFormat(date, highlighted_format)





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


