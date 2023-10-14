#LoginForm.py

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from model.admin_model import DatabaseHandler


class LoginWindow(QWidget):
    def __init__(self, db_path, main_window):
        super().__init__()
        self.db_path = db_path
        self.main_window = main_window
        self.db_handler = DatabaseHandler(db_path)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.returnPressed.connect(self.login)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.username_input.returnPressed.connect(self.password_input.setFocus)

        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.db_handler.validate_credentials(username, password):
            self.main_window.show_principal_view()
        else:
            self.show_error_dialog()



    def show_error_dialog(self):
        error_dialog = QMessageBox()
        error_dialog.setWindowTitle("Login Error")
        error_dialog.setText("Invalid username or password. Please try again.")
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.exec_()

    def show(self):
        # Reset the input fields when the window is shown again
        self.username_input.setText("")
        self.password_input.setText("")
        super().show()