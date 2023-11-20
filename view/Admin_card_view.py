import typing
from PyQt5.QtWidgets import QWidget,QCheckBox,QGraphicsDropShadowEffect, QLineEdit,QVBoxLayout, QLabel , QFrame , QHBoxLayout,QPushButton , QMessageBox
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter 
from PyQt5.QtCore import Qt
from controller.team_crud_controller import AdminCrudController

class AdminAccountCard(QWidget):
    def __init__(self , id_admin, adminname , adminpassword):
        super().__init__()

        self.id_admin = id_admin
        self.adminname = adminname
        self.adminpassword = adminpassword


        self.container = QWidget()
        self.container.setObjectName("card-container")
        self.container.setStyleSheet("#card-container { border: 1px solid black; border-radius: 5px; margin: 10px; padding: 10px; }")
        self.controller = AdminCrudController(db_path='data/my_database.sqlite')

        self.adminname_label = QLineEdit(f"{self.adminname}")
        self.adminpassword_label = QLineEdit(f"{self.adminpassword}")
        self.adminpassword_label.setReadOnly(True)  # Set it to read-only initially
        self.adminpassword_label.setEchoMode(QLineEdit.Password)


        self.show_password_checkbox = QCheckBox("Montrer")
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)

        password_layout = QHBoxLayout()
        password_layout.addWidget(self.adminpassword_label)
        password_layout.addWidget(self.show_password_checkbox)


        self.edit_button = QPushButton("Modifier")
        self.edit_button.setObjectName("edit-button")
        self.edit_button.setStyleSheet("#edit-button { background-color: #7ed957; color: #102429; }")
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
        self.delete_button.setStyleSheet("#delete-button { background-color: #404040; color: white; }")
        self.delete_button.clicked.connect(self.confirm_delete)

        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch(1)  # Pour pousser le bouton à droite
        top_right_layout.addWidget(self.edit_button)
        top_right_layout.addWidget(self.save_button)
        top_right_layout.addWidget(self.cancel_button)
        top_right_layout.addWidget(self.delete_button)
        

        card_layout = QVBoxLayout()
        card_layout.addWidget(self.adminname_label)
        card_layout.addLayout(password_layout)
        card_layout.addLayout(top_right_layout)
        self.container.setLayout(card_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)

    def confirm_delete(self):
        idAdminStr = str(self.id_admin)
        # Affichez une boîte de dialogue de confirmation
        confirmation = QMessageBox.question(self, f"Confirmation", "Êtes-vous sûr de vouloir supprimer le compte ?",
                                             QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.controller.delete_Admin(idAdminStr)
            self.deleteLater()

    def toggle_editable(self):
        self.adminname_label.setReadOnly(False)
        self.adminpassword_label.setReadOnly(False)
        self.edit_button.hide()
        self.save_button.show()
        self.cancel_button.show()

    def save_changes(self):
        new_username = self.adminname_label.text()
        new_password = self.adminpassword_label.text()

        if new_username != self.adminname:
            self.controller.update_adminName(self.id_admin, new_username)
            self.adminname = new_username

        if new_password != self.adminpassword:
            self.controller.update_adminPassword(self.id_admin, new_password)
            self.adminpassword = new_password

        # Restore the original view
        self.adminname_label.setReadOnly(True)
        self.adminpassword_label.setReadOnly(True)
        self.edit_button.show()
        self.save_button.hide()
        self.cancel_button.hide()

    def cancel_changes(self):
        # Restore the original data and view
        self.adminname_label.setText(self.adminname)
        self.adminpassword_label.setText(self.adminpassword)
        self.adminname_label.setReadOnly(True)
        self.adminpassword_label.setReadOnly(True)
        self.edit_button.show()
        self.save_button.hide()
        self.cancel_button.hide()

    def toggle_password_visibility(self, state):
        if state == Qt.Checked:
            self.adminpassword_label.setReadOnly(False)
            self.adminpassword_label.setEchoMode(QLineEdit.Normal)
        else:
            self.adminpassword_label.setReadOnly(True)
            self.adminpassword_label.setEchoMode(QLineEdit.Password)