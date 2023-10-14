import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QVBoxLayout
from controller.personnel_card_controller import PersonnelController

class EmployeeDetailsForm(QWidget):
    def __init__(self, badge):
        super().__init__()
        self.badge = badge
        self.controller = PersonnelController(db_path='data/my_database.sqlite')
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

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Replace 'your_badge_data' with the actual badge data you want to test
    badge_data = '543454'
    
    # Create an instance of EmployeeDetailsForm
    details_form = EmployeeDetailsForm(badge_data)

    # Show the form
    details_form.show()

    sys.exit(app.exec_())