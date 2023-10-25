import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from PyQt5.QtWidgets import QPushButton,QApplication,QWidget, QLabel, QVBoxLayout
from controller.personnel_card_controller import PersonnelController

class EmployeeDetailsForm(QWidget):
    def __init__(self, badge , main_window):
        super().__init__()
        self.badge = badge
        self.main_window = main_window
        self.controller = PersonnelController(db_path='data\my_database.sqlite')
        employee_data = self.controller.get_employee_details(self.badge)
        self.initUI(employee_data)

    def initUI(self, employee_data):
        layout = QVBoxLayout()

        if employee_data:
            for value in employee_data:
                label = QLabel(f" {value}\n")
                layout.addWidget(label)
        else:
            label = QLabel("Employee not found")  # Add a message if employee is not found
            layout.addWidget(label)

        # Add the "Previous" button
        previous_button = QPushButton("Previous")
        previous_button.clicked.connect(self.show_previous_cards)
        layout.addWidget(previous_button)
        self.setLayout(layout)

    def show_previous_cards(self):
        print("previous function called")
        # Use the reference to the main window to switch back to the list of cards
        if self.main_window:
            print("inside the condition if self.mainwindow")
            self.main_window.return_to_last_displayed_page(self)
        else:
            self.main_window.setupUI()
            self.main_window.setCentralWidget(self.main_window.container)

