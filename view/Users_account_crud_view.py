from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class User_account(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("USERS CRUD HERE")
        layout.addWidget(label)
        self.setLayout(layout)