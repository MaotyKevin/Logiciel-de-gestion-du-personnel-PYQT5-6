# card_view.py

from PyQt5.QtWidgets import QWidget,QGraphicsDropShadowEffect, QVBoxLayout, QLabel , QFrame , QHBoxLayout,QPushButton , QMessageBox
from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter 
from PyQt5.QtCore import Qt
from controller.personnel_card_controller import PersonnelController
from view.employee_detail_view import EmployeeDetailsForm


class Card(QWidget):
    def __init__(self, badge=None, nom=None, categorie=None,fonction=None, sous_categorie=None, main_window=None ):
        super().__init__()
        

        # Conteneur principal pour la carte
        self.container = QWidget()
        self.container.setObjectName("card-container")
        self.container.setStyleSheet("#card-container { border: 1px solid gray; border-radius: 5px; margin: 10px; padding: 10px;}")

        self.controller = PersonnelController(db_path='data\my_database.sqlite')

        

        # Créez des étiquettes pour les informations de la carte
        badge_label = QLabel(f"Badge: {badge}")
        self.badge = badge
        nom_label = QLabel(f"Nom: {nom}")
        fonction_label = QLabel(f"Fonction: {fonction}")
        categorie_label = QLabel(f"Categorie: {categorie}")
        sous_categorie_label = QLabel(f"Sous-Categorie: {sous_categorie}")

        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setObjectName("delete-button")
        self.delete_button.setStyleSheet("#delete-button { background-color: #FF7519; color: white; }")
        self.delete_button.clicked.connect(self.confirm_delete)  # Connectez le signal clicked au slot confirm_delete

        self.detail_utton = QPushButton("Details")
        self.detail_utton.setObjectName("details-button")
        self.detail_utton.setStyleSheet("#details-button { background-color: #007BFF; color: white; }")
        self.detail_utton.clicked.connect(self.show_employee_details)

        # Créez un layout horizontal pour le coin supérieur droit
        top_right_layout = QHBoxLayout()
        top_right_layout.addStretch(1)  # Pour pousser le bouton à droite
        top_right_layout.addWidget(self.detail_utton)
        top_right_layout.addWidget(self.delete_button)


        # Ajoutez les étiquettes au conteneur de la carte
        card_layout = QVBoxLayout()
        card_layout.addWidget(badge_label)
        card_layout.addWidget(nom_label)
        card_layout.addWidget(fonction_label)
        card_layout.addWidget(categorie_label)
        card_layout.addWidget(sous_categorie_label)
        card_layout.addLayout(top_right_layout)
        self.container.setLayout(card_layout)

        # Ajoutez le conteneur au widget principal (cette classe Card)
        layout = QVBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)

        self.open_employee_details = None
        self.main_window = main_window
        self.employee_details_form = EmployeeDetailsForm(self.badge , main_window)

    def show_employee_details(self):
        # Use the reference to the main window to switch views
        if self.main_window:
            self.main_window.show_employee_details_view(self.employee_details_form)
        

    def confirm_delete(self):
        badge_str = str(self.badge)
        # Affichez une boîte de dialogue de confirmation
        confirmation = QMessageBox.question(self, "Confirmation", "Êtes-vous sûr de vouloir supprimer cette carte ?",
                                             QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.controller.delete_data(badge_str)
            self.deleteLater()


