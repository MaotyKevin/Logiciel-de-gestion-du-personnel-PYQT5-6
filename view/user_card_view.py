import typing
from PyQt5.QtWidgets import QWidget,QGraphicsDropShadowEffect, QVBoxLayout, QLabel , QFrame , QHBoxLayout,QPushButton , QMessageBox
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter 
from PyQt5.QtCore import Qt
from controller.team_crud_controller import AdminCrudController

class UserCard(QWidget):
    def __init__(self , id_user, username , password):
        super().__init__()

        self.id_user = id_user
        self.username = username
        self.password = password


        self.container = QWidget()
        self.container.setObjectName("card-container")
        self.container.setStyleSheet("#card-container { border: 1px solid black; border-radius: 5px; margin: 10px; padding: 10px; }")
        self.controller = AdminCrudController(db_path='data/my_database.sqlite')

        username_label = QLabel(f"{self.username}")
        password_label = QLabel(f"{self.password}")

        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setObjectName("delete-button")
        self.delete_button.setStyleSheet("#delete-button { background-color: red; color: white; }")
        self.delete_button.clicked.connect(self.confirm_delete)

        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch(1)  # Pour pousser le bouton à droite
        top_right_layout.addWidget(self.delete_button)

        card_layout = QVBoxLayout()
        card_layout.addWidget(username_label)
        card_layout.addWidget(password_label)
        card_layout.addLayout(top_right_layout)
        self.container.setLayout(card_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)

    def confirm_delete(self):
        idUserStr = str(self.id_user)
        # Affichez une boîte de dialogue de confirmation
        confirmation = QMessageBox.question(self, "Confirmation", "Êtes-vous sûr de vouloir supprimer cette equipe ?",
                                             QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.controller.delete_User(idUserStr)
            self.deleteLater()