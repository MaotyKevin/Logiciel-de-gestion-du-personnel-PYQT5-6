# page2_view.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QGridLayout
from view.card_view import Card
from controller.personnel_card_controller import PersonnelController
from PyQt5 import QtCore

class Personnal_Card(QWidget):
    def __init__(self, db_path):
        super().__init__()
        self.db_path = db_path
        self.controller = PersonnelController(db_path)
        self.personnel_data = []
        self.donnee = self.controller.get_personnel_data()
        self.initUI()
        
    def initUI(self):
        # Créez un layout pour les cartes avec QGridLayout
        self.page2_layout = QGridLayout()
        self.page2_layout.setAlignment(QtCore.Qt.AlignTop)  # Alignez les widgets en haut

        # Créez un widget qui peut être défilé
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        # Créez un widget conteneur pour le layout
        container = QWidget()
        container.setLayout(self.page2_layout)
        #container.setStyleSheet("border: 1px solid black")
        
        # Définissez le widget conteneur comme widget pour la zone défilante
        scroll_area.setWidget(container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def refresh_personnel_cards(self, personnel_data=None):
        # Supprimez toutes les cartes actuelles
        for i in reversed(range(self.page2_layout.count())):
            widget = self.page2_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Utilisez les résultats filtrés ou les données complètes du personnel
        data = personnel_data or self.controller.get_personnel_data()
        print(data)
        for row_idx, row in enumerate(data):
            badge, nom, categorie, fonction, sous_categorie = row
            card = Card(badge, nom, categorie, fonction, sous_categorie)
            self.page2_layout.addWidget(card, row_idx // 3, row_idx % 3)

        # Actualisez l'affichage
        self.update()