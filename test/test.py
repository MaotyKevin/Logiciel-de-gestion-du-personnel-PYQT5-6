import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel

class AdminPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        user_crud_button = QPushButton("User CRUD")
        team_crud_button = QPushButton("Team CRUD")
        layout.addWidget(user_crud_button)
        layout.addWidget(team_crud_button)
        self.setLayout(layout)

class UserCrudPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        # Add user CRUD elements here
        label = QLabel("User CRUD Page")
        layout.addWidget(label)
        self.setLayout(layout)

class TeamCrudPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        # Add team CRUD elements here
        label = QLabel("Team CRUD Page")
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Panel")
        self.setGeometry(100, 100, 800, 600)

        self.stacked_widget = QStackedWidget()

        self.admin_page = AdminPage()
        self.user_crud_page = UserCrudPage()
        self.team_crud_page = TeamCrudPage()

        self.stacked_widget.addWidget(self.admin_page)
        self.stacked_widget.addWidget(self.user_crud_page)
        self.stacked_widget.addWidget(self.team_crud_page)

        self.setCentralWidget(self.stacked_widget)

        # Connect buttons to page changes
        self.admin_page.layout().itemAt(0).widget().clicked.connect(self.show_user_crud)
        self.admin_page.layout().itemAt(1).widget().clicked.connect(self.show_team_crud)

    def show_user_crud(self):
        self.stacked_widget.setCurrentWidget(self.user_crud_page)

    def show_team_crud(self):
        self.stacked_widget.setCurrentWidget(self.team_crud_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
