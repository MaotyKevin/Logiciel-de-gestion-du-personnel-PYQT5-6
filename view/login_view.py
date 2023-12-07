#LoginForm.py

import sys
from PyQt5.QtWidgets import QApplication,QSplitter, QWidget, QHBoxLayout,QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox 
from PyQt5 import QtGui
from PyQt5.QtCore import QRect  , QTimer
from PyQt5 import QtCore 
from PyQt5.QtGui import QIcon

from model.admin_model import DatabaseHandler


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
        right_widget.setStyleSheet("background-color: #102429;")
        right_layout = QHBoxLayout()


        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("width : 200; height: 30;color:white;font-weight:bold; background-color:#102429;border-radius:5px;padding: 10px 20px;border:1px solid white;")
        self.username_input.setPlaceholderText("Pseudo")


        self.toggle_button = QPushButton()
        self.toggle_button.setIcon(QIcon("assets/pic/hidden-eye.svg"))
        self.toggle_button.setFlat(True)
        self.toggle_button.clicked.connect(self.on_toggle_password_Action)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.returnPressed.connect(self.login)
        self.password_input.setPlaceholderText("mot de passe")
        self.password_input.setStyleSheet("width : 200; height: 30;color:white;font-weight:bold;background-color:#102429;border-radius:5px;padding: 10px 20px;border:1px solid white;")

        self.username_input.returnPressed.connect(self.password_input.setFocus)
        

        #self.login_button = QPushButton("Login")
        #self.login_button.clicked.connect(self.login)



        #right_layout.addWidget(QLabel("Username:"))
        right_layout.addWidget(self.username_input)
        #right_layout.addWidget(QLabel("Password:"))
        right_layout.addWidget(self.password_input)
        right_layout.addWidget(self.toggle_button)
        #right_layout.addWidget(self.login_button)

        welcome = QLabel("")
        welcome.setStyleSheet("color: #7ed957; font-size: 16px; font-weight: light;")


        vertical = QVBoxLayout()
        vertical.addStretch(1)
        vertical.addWidget(welcome)
        vertical.addLayout(right_layout)
        vertical.addStretch(1)

        right_widget.setLayout(vertical)

        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)

        main_layout.addWidget(splitter)

        # Set the main layout for the central widget
        self.setLayout(main_layout)

        self.password_shown = False

        self.welcome_text = "Welcome , please log In here...."
        self.current_index = 0
        self.welcome_timer = QTimer(self)
        self.welcome_timer.timeout.connect(self.update_welcome_label)
        self.welcome_timer.start(100)  # Set the interval (milliseconds) between letters

    def update_welcome_label(self):
        if self.current_index < len(self.welcome_text):
            current_letter = self.welcome_text[self.current_index]
            self.findChild(QLabel).setText(self.findChild(QLabel).text() + current_letter)
            self.current_index += 1
        else:
            self.welcome_timer.stop()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        id , usernames, role = self.db_handler.validate_credentials(username, password)

        if role == "Admin":
            
            self.main_window.show_principal_view()
            self.main_window.setLoggedUserInfo(usernames)
        elif role == "User":
            #self.show_user_dialog(usernames)
            self.main_window.show_client_message(id , usernames)
        else:
            self.show_error_dialog()



    def show_error_dialog(self):
        error_dialog = QMessageBox()
        error_dialog.setWindowTitle("Erreur de connexion")
        error_dialog.setText("Pseudo ou mot de passe invalide , reessayez.")
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.exec_()

    def show_user_dialog(self , username):
        user_dialog = QMessageBox()
        user_dialog.setWindowTitle("User confirmed")
        user_dialog.setText(f"{username} est connectee , GUI maintenance.")
        user_dialog.setIcon(QMessageBox.Warning)
        user_dialog.exec_()

    def clear(self):
        # Reset the input fields when the window is shown again
        self.username_input.setText("")
        self.password_input.setText("")
        #super().show()

    def on_toggle_password_Action(self):
        if not self.password_shown:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.password_shown = True
            self.toggle_button.setIcon(QIcon("assets/pic/visible-eye.svg"))
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.password_shown = False
            self.toggle_button.setIcon(QIcon("assets/pic/hidden-eye.svg"))