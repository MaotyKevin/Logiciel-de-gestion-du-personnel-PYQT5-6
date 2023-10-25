import typing
from PyQt5.QtWidgets import QWidget,QGraphicsDropShadowEffect, QVBoxLayout, QLabel , QFrame , QHBoxLayout,QPushButton , QMessageBox
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter 
from PyQt5.QtCore import Qt
from controller.team_crud_controller import AdminCrudController

class TeamCard(QWidget):
    def __init__(self , id_equipe, nom_equipe):
        super().__init__()

        self.id_equipe = id_equipe

        self.container = QWidget()
        self.container.setObjectName("card-container")
        self.container.setStyleSheet("#card-container { border: 1px solid black; border-radius: 5px; margin: 10px; padding: 10px; }")
        self.controller = AdminCrudController(db_path='data/my_database.sqlite')

        equipe_label = QLabel(f"{nom_equipe}")
        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setObjectName("delete-button")
        self.delete_button.setStyleSheet("#delete-button { background-color: red; color: white; }")
        self.delete_button.clicked.connect(self.confirm_delete)

        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch(1)  # Pour pousser le bouton à droite
        top_right_layout.addWidget(self.delete_button)

        card_layout = QVBoxLayout()
        card_layout.addWidget(equipe_label)
        card_layout.addLayout(top_right_layout)
        self.container.setLayout(card_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)

    def confirm_delete(self):
        idTeamStr = str(self.id_equipe)
        # Affichez une boîte de dialogue de confirmation
        confirmation = QMessageBox.question(self, "Confirmation", "Êtes-vous sûr de vouloir supprimer cette equipe ?",
                                             QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.controller.delete_data(idTeamStr)
            self.deleteLater()