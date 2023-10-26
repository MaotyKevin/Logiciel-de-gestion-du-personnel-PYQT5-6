import typing
from PyQt5.QtWidgets import QWidget,QLineEdit,QGraphicsDropShadowEffect, QVBoxLayout, QLabel , QFrame , QHBoxLayout,QPushButton , QMessageBox
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter 
from PyQt5.QtCore import Qt
from controller.team_crud_controller import AdminCrudController

class SCCard(QWidget):
    def __init__(self , id_sousCategorie, sousCategorie):
        super().__init__()

        self.id_sousCategorie = id_sousCategorie
        self.sousCategorie = sousCategorie

        self.container = QWidget()
        self.container.setObjectName("card-container")
        self.container.setStyleSheet("#card-container { border: 1px solid black; border-radius: 5px; margin: 10px; padding: 10px; }")
        self.controller = AdminCrudController(db_path='data/my_database.sqlite')

        self.SC_label = QLineEdit(f"{self.sousCategorie}")
        self.SC_label.setStyleSheet("font-weight: semi-bold;")

        self.edit_button = QPushButton("Modifier")
        self.edit_button.setObjectName("edit-button")
        self.edit_button.setStyleSheet("#edit-button { background-color: #007BFF; color: white; }")
        self.edit_button.clicked.connect(self.toggle_editable)


        self.save_button = QPushButton("Enregistrer")
        self.save_button.setObjectName("save-button")
        self.save_button.setStyleSheet("#save-button { background-color: green; color: white; }")
        self.save_button.clicked.connect(self.save_changes)
        self.save_button.hide()  # Initially hide the "Save" button

        self.cancel_button = QPushButton("Annuler")
        self.cancel_button.setObjectName("cancel-button")
        self.cancel_button.setStyleSheet("#cancel-button { background-color: #007BFF; color: white; }")
        self.cancel_button.clicked.connect(self.cancel_changes)
        self.cancel_button.hide()  # Initially hide the "Cancel" button

        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setObjectName("delete-button")
        self.delete_button.setStyleSheet("#delete-button { background-color: #FF7519; color: white; }")
        self.delete_button.clicked.connect(self.confirm_delete)


        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch(1)  # Pour pousser le bouton à droite
        top_right_layout.addWidget(self.edit_button)
        top_right_layout.addWidget(self.save_button)
        top_right_layout.addWidget(self.cancel_button)
        top_right_layout.addWidget(self.delete_button)
        
        card_layout = QVBoxLayout()
        card_layout.addWidget(self.SC_label)
        card_layout.addLayout(top_right_layout)
        self.container.setLayout(card_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)

    def confirm_delete(self):
        idSCStr = str(self.id_sousCategorie)
        # Affichez une boîte de dialogue de confirmation
        confirmation = QMessageBox.question(self, "Confirmation", "Êtes-vous sûr de vouloir supprimer cette equipe ?",
                                             QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.controller.delete_team(idSCStr)
            self.deleteLater()

    def toggle_editable(self):
        self.SC_label.setReadOnly(False)
        self.edit_button.hide()
        self.save_button.show()
        self.cancel_button.show()

    def save_changes(self):
        newSC = self.SC_label.text()

        if newSC != self.sousCategorie:
            self.controller.updateSC(self.id_sousCategorie, newSC)
            self.sousCategorie = newSC


        # Restore the original view
        self.SC_label.setReadOnly(True)
      
        self.edit_button.show()
        self.save_button.hide()
        self.cancel_button.hide()

    def cancel_changes(self):
        # Restore the original data and view
        self.SC_label.setText(self.sousCategorie)
       
        self.SC_label.setReadOnly(True)
   
        self.edit_button.show()
        self.save_button.hide()
        self.cancel_button.hide()