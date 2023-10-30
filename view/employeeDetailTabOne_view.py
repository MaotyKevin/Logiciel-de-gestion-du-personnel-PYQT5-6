import sys , os
from PyQt5.QtWidgets import QApplication,QStackedWidget, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog,QScrollArea , QDateEdit , QMessageBox , QSizePolicy
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter
from PyQt5.QtCore import Qt , QDate, pyqtSignal , QRect
from controller.personnel_card_controller import PersonnelController

class EmployeeDetailsTabOne(QWidget):
    def __init__(self , badge):
        super().__init__()
        self.badge = badge
        self.controller = PersonnelController(db_path='data\my_database.sqlite')
        employee_data = self.controller.get_employee_details(self.badge)
        self.defUI(employee_data)

    def defUI(self , employee_data):
        layout = QVBoxLayout()

        if employee_data:
            Badge , Nom , Sexe = employee_data

            self.badgeLabel = QLineEdit(f"Badge : {Badge}")
            self.badgeLabel.setReadOnly(True)
            self.styleLineEdit(self.badgeLabel)

            self.NomLabel = QLineEdit(f"Nom : {Nom}")
            self.NomLabel.setReadOnly(True)
            self.styleLineEdit(self.NomLabel)

            self.SexeLabel = QLineEdit(f"Sexe : {Sexe}")
            self.SexeLabel.setReadOnly(True)
            self.styleLineEdit(self.SexeLabel)

            badge_desired_width = self.badgeLabel.fontMetrics().width(self.badgeLabel.text()) + 20
            self.badgeLabel.setFixedWidth(badge_desired_width)

            nom_desired_width = self.NomLabel.fontMetrics().width(self.NomLabel.text()) + 20
            self.NomLabel.setFixedWidth(nom_desired_width)

            sexe_desired_width = self.SexeLabel.fontMetrics().width(self.SexeLabel.text()) + 20
            self.SexeLabel.setFixedWidth(sexe_desired_width)

            layout.addWidget(self.badgeLabel)
            layout.addWidget(self.NomLabel)
            layout.addWidget(self.SexeLabel)   

             
        self.setLayout(layout)

    def styleLineEdit(self, line_edit):
        # Define the CSS style for QLineEdit
        style = """
            QLineEdit {
                background-color: black;  /* Background color */
                color:white;
                border : none;
                border-bottom: 1px solid #C0C0C0;  /* Border color and thickness */
                border-radius: 5px;         /* Rounded corners */
                padding: 5px;               /* Padding inside the QLineEdit */
                
            }
        """
        line_edit.setStyleSheet(style)







