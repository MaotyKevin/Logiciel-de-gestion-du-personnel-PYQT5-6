#LoginForm.py

from PyQt5.QtWidgets import QApplication,QSplitter, QWidget, QHBoxLayout,QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from model.admin_model import DatabaseHandler
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class LoginWindow(QWidget):
    def __init__(self, db_path, main_window):
        super().__init__()
        self.db_path = db_path
        self.main_window = main_window
        self.db_handler = DatabaseHandler(db_path)

        main_layout = QHBoxLayout()

        splitter = QSplitter()

        left_widget = QWidget()
        left_widget.setStyleSheet("background-color:white;")
        left_layout = QHBoxLayout()
        left_label = QLabel()
        
        # Load the background image
        background_image = QtGui.QPixmap("assets\pic\Fanahisoa.jpg")
        # Resize the background image to your desired dimensions
        background_image = background_image.scaled(700, 300)  # Adjust the size as needed
        left_label.setPixmap(background_image)

        left_layout.addWidget(left_label)
        left_widget.setLayout(left_layout)

        right_widget = QWidget()
        #right_widget.setStyleSheet("background-color: black;")
        right_layout = QHBoxLayout()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.returnPressed.connect(self.login)
        self.username_input.setStyleSheet("width : 200; height: 30;")
        self.username_input.setPlaceholderText("Username")
        self.password_input.setPlaceholderText("password")
        self.password_input.setStyleSheet("width : 200; height: 30;")

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.username_input.returnPressed.connect(self.password_input.setFocus)

        #right_layout.addWidget(QLabel("Username:"))
        right_layout.addWidget(self.username_input)
        #right_layout.addWidget(QLabel("Password:"))
        right_layout.addWidget(self.password_input)
        right_layout.addWidget(self.login_button)
        right_widget.setLayout(right_layout)

        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)

        main_layout.addWidget(splitter)

        # Set the main layout for the central widget
        self.setLayout(main_layout)

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

    def clear(self):
        # Reset the input fields when the window is shown again
        self.username_input.setText("")
        self.password_input.setText("")
        #super().show()