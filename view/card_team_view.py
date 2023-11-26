import typing
from PyQt5.QtWidgets import QWidget,QLineEdit,QGraphicsDropShadowEffect, QVBoxLayout, QLabel , QFrame , QHBoxLayout,QPushButton , QMessageBox
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter 
from PyQt5.QtCore import Qt
from controller.team_crud_controller import AdminCrudController

class TeamCard(QWidget):
    def __init__(self , id_equipe, nom_equipe):
        super().__init__()

        self.id_equipe = id_equipe
        self.nom_equipe = nom_equipe

        self.container = QWidget()
        self.container.setObjectName("card-container")
        self.container.setStyleSheet("#card-container { border: 1px solid black; border-radius: 5px; margin: 10px; padding: 10px; }")
        self.controller = AdminCrudController(db_path='data/my_database.sqlite')

        self.equipe_label = QLineEdit(f"{self.nom_equipe}")
        self.equipe_label.setStyleSheet("font-weight: semi-bold;")

        self.edit_button = QPushButton("Modifier")
        self.edit_button.setObjectName("edit-button")
        self.edit_button.setStyleSheet("#edit-button { background-color: #7ed957; color: #102429; }")
        self.edit_button.clicked.connect(self.toggle_editable)


        self.save_button = QPushButton("Enregistrer")
        self.save_button.setObjectName("save-button")
        self.save_button.setStyleSheet("#save-button { background-color: white; color: #102429; border: 1px solid #102429 }")
        self.save_button.clicked.connect(self.save_changes)
        self.save_button.hide()  # Initially hide the "Save" button

        self.cancel_button = QPushButton("Annuler")
        self.cancel_button.setObjectName("cancel-button")
        self.cancel_button.setStyleSheet("#cancel-button { background-color: #7ed957; color: #102429; }")
        self.cancel_button.clicked.connect(self.cancel_changes)
        self.cancel_button.hide()  # Initially hide the "Cancel" button

        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setObjectName("delete-button")
        self.delete_button.setStyleSheet("#delete-button { background-color: #404040; color: white; }")
        self.delete_button.clicked.connect(self.confirm_delete)


        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch(1)  # Pour pousser le bouton à droite
        top_right_layout.addWidget(self.edit_button)
        top_right_layout.addWidget(self.save_button)
        top_right_layout.addWidget(self.cancel_button)
        top_right_layout.addWidget(self.delete_button)
        
        card_layout = QVBoxLayout()
        card_layout.addWidget(self.equipe_label)
        card_layout.addLayout(top_right_layout)
        self.container.setLayout(card_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)

    def confirm_delete(self):
        idTeamStr = str(self.id_equipe)

        if self.controller.verifyEmployeeTeam(idTeamStr):
            QMessageBox.warning(self, "Attention", "Impossible d'effacer l'equipe car des employés y sont encore.")
            return

        # Affichez une boîte de dialogue de confirmation
        confirmation = QMessageBox.question(self, "Confirmation", "Êtes-vous sûr de vouloir supprimer cette equipe ?",
                                             QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.controller.delete_team(idTeamStr)
            self.deleteLater()

    def toggle_editable(self):
        self.equipe_label.setReadOnly(False)
        self.edit_button.hide()
        self.save_button.show()
        self.cancel_button.show()

    def save_changes(self):
        newEquipe = self.equipe_label.text()

        if newEquipe != self.nom_equipe:
            self.controller.update_team(self.id_equipe, newEquipe)
            self.nom_equipe = newEquipe


        # Restore the original view
        self.equipe_label.setReadOnly(True)
      
        self.edit_button.show()
        self.save_button.hide()
        self.cancel_button.hide()

    def cancel_changes(self):
        # Restore the original data and view
        self.equipe_label.setText(self.nom_equipe)
       
        self.equipe_label.setReadOnly(True)
   
        self.edit_button.show()
        self.save_button.hide()
        self.cancel_button.hide()