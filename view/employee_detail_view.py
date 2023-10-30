import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from PyQt5.QtWidgets import QPushButton,QApplication,QWidget, QLabel, QVBoxLayout , QTabWidget , QScrollArea , QHBoxLayout 
from controller.personnel_card_controller import PersonnelController
from view.employeeDetailTabOne_view import EmployeeDetailsTabOne

class EmployeeTabForm(QTabWidget):
    def __init__(self , badge):
        super().__init__()
        
        self.badge = badge
        tab1 = EmployeeDetailsTabOne(self.badge)
        tab2 = QWidget()

        self.addTab(tab1 , "tab1")
        self.addTab(tab2 , "tab2")
        

class EmployeeDetailsForm(QWidget):
    def __init__(self, badge , main_window):
        super().__init__()
        self.badge = badge
        print(f"BADGE DANS DETAILS FORM = {self.badge}")
        self.main_window = main_window
        self.employeeTabForm = EmployeeTabForm(self.badge)

        self.initUI()

    def initUI(self):

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.employeeTabForm)  # Set the QTabWidget as the widget within the scroll area
        scroll_area.setWidgetResizable(True) 
        container = QWidget()
        container_layout = QVBoxLayout()
        previous_button = QPushButton("Previous")
        previous_button.clicked.connect(self.show_previous_cards)
        container_layout.addWidget(previous_button)
        container_layout.addWidget(scroll_area)
        
        # Add the "Previous" button to the container

        

        container.setLayout(container_layout)

        layout = QVBoxLayout()
        layout.addWidget(container)  # Add the container widget to the layout
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

