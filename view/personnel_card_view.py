# page2_view.py
import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from PyQt5.QtWidgets import QComboBox,QWidget, QVBoxLayout, QLabel, QScrollArea, QGridLayout ,QFrame
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
        container.setStyleSheet("background-color: white")
        
        # Définissez le widget conteneur comme widget pour la zone défilante
        scroll_area.setWidget(container)

        # Create a combo box for team selection
        self.team_filter = QComboBox()
        self.team_filter.addItem("All Teams") 
         # Initial option
        self.equipe_name = self.controller.get_team_names()
        self.team_filter.addItems(self.equipe_name)  # Implement this method to get team names
        self.team_filter.currentIndexChanged.connect(self.filter_personnel_team)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.team_filter)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def filter_personnel_team(self, index):
        selected_team = self.team_filter.currentText()
        personnel_data = self.controller.get_personnel_by_team(selected_team)
        self.refresh_personnel_cards(personnel_data)

    def refresh_personnel_cards(self, personnel_data=None):
        # Supprimez toutes les cartes actuelles
        for i in reversed(range(self.page2_layout.count())):
            widget = self.page2_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

            # Utilisez les résultats filtrés ou les données complètes du personnel
        if personnel_data is not None:

                data = personnel_data 
        else: 
                data = self.controller.get_personnel_data()
    
        #data = self.controller.get_personnel_data or personnel_data
        if data is not None:
            print(f"DATA = {data}")
            for row_idx, row in enumerate(data):
                badge, nom, categorie, fonction, sous_categorie = row
                card_container = QFrame()
                card_container = Card( badge, nom, categorie, fonction, sous_categorie)
                self.page2_layout.addWidget(card_container, row_idx // 3, row_idx % 3)

                card_container.setStyleSheet(" border-radius: 2px; padding: 5px ; margin :5px")

                # Actualisez l'affichage
            self.update()