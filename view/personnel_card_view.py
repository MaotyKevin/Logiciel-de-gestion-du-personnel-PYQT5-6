# page2_view.py
import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from PyQt5.QtWidgets import QComboBox,QHBoxLayout,QWidget, QVBoxLayout, QLabel, QScrollArea, QGridLayout ,QFrame , QLineEdit
from view.card_view import Card
from controller.personnel_card_controller import PersonnelController
from PyQt5 import QtCore
from PyQt5.QtCore import QRect , Qt

class Personnal_Card(QWidget):
    def __init__(self, db_path , main_window):
        super().__init__()
        self.db_path = db_path
        self.main_window = main_window
        self.controller = PersonnelController(db_path)
        self.personnel_data = []
        self.donnee = self.controller.get_personnel_data()
        self.initUI()
        
    def initUI(self):
        self.cardCount = 0
        # Créez un layout pour les cartes avec QGridLayout
        self.page2_layout = QGridLayout()
        self.page2_layout.setAlignment(QtCore.Qt.AlignTop)  # Alignez les widgets en haut

        # Créez un widget qui peut être défilé
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setStyleSheet(
            """
            QScrollArea {
                border: 1px solid #CCCCCC;
            }
            
            QScrollBar:vertical {
                border: 1px solid white;
                background: #102429;
                width: 12px;
                margin: 0px;
            }
            
            QScrollBar:horizontal {
                border: 1px solid white;
                background: #102429;
                height: 12px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #102429;
                min-height: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::handle:horizontal {
                background: #102429;
                min-width: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
            }
            """
        )

        
        # Créez un widget conteneur pour le layout
        container = QWidget()
        container.setLayout(self.page2_layout)
        container.setStyleSheet("background-color: white;")
        
        # Définissez le widget conteneur comme widget pour la zone défilante
        scroll_area.setWidget(container)

        self.employee_count_label = QLabel()
        self.employee_count_label.setStyleSheet("font-size: 14px; color: #333333;font-weight:bold;")

        # Create a combo box for team selection
        combo_container = QHBoxLayout()

        self.search_field = QLineEdit()  # Champ de recherche
        self.search_field.textChanged.connect(self.perform_search)
        self.search_field.setPlaceholderText("Rechercher par Badge ou Nom...")
        self.search_field.setStyleSheet("Background-color: #FFFFFF;border: 1px solid #CCCCCC; border-radius: 5px; padding: 5px;font-size: 14px;color: #333333;width : 250px;")


        self.team_filter = QComboBox()
        self.team_filter.addItem("All Teams")

        self.Categ_filter = QComboBox()
        self.Categ_filter.addItem("All Categ")

        self.SC_filter = QComboBox()
        self.SC_filter.addItem("All SC")

        combo_container.addWidget(self.employee_count_label)
        combo_container.addStretch(1)
        combo_container.addWidget(self.team_filter)
        combo_container.addSpacing(10)
        combo_container.addWidget(self.Categ_filter)
        combo_container.addSpacing(10)
        combo_container.addWidget(self.SC_filter)
        combo_container.addSpacing(10)
        combo_container.addWidget(self.search_field)
        
        self.team_filter.setStyleSheet("QComboBox { padding: 5px; border:1px solid #CCCCCC; border-radius: 5px; background-color:#102429;color:white;}     QComboBox::down-arrow {background-color: #7ed957;}")
        self.Categ_filter.setStyleSheet("QComboBox { padding: 5px; border:1px solid #CCCCCC; border-radius: 5px; background-color:#102429;color:white;}     QComboBox::down-arrow {background-color: #7ed957;}")
        self.SC_filter.setStyleSheet("QComboBox { padding: 5px; border:1px solid #CCCCCC; border-radius: 5px;background-color:#102429;color:white; } QComboBox::down-arrow {background-color: #7ed957;}")

         # Initial option
        self.equipe_name = self.controller.get_team_names()
        self.team_filter.addItems(self.equipe_name)  # Implement this method to get team names
        self.team_filter.currentIndexChanged.connect(self.filter_personnel_team)

        self.SC_name = self.controller.get_SC_names()
        self.SC_filter.addItems(self.SC_name)  # Implement this method to get team names
        self.SC_filter.currentIndexChanged.connect(self.filter_personnel_SC)

        self.Categ_name = self.controller.get_categ_names()
        self.Categ_filter.addItems(self.Categ_name)  # Implement this method to get team names
        self.Categ_filter.currentIndexChanged.connect(self.filter_personnel_Categorie)

        #combo_container.setStretch(1000 , 1000)
        #combo_container.setSpacing(20)
        #combo_container.addStretch(900)
        #combo_container.setContentsMargins(550 , 0 , 0 , 0)
        #combo_container.setGeometry(QRect(1000 , 100 , 100 , 100))
        main_layout = QVBoxLayout()
        main_layout.addLayout(combo_container)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        self.update_employee_count(self.cardCount)

    def update_employee_count(self , card_count):
        # Count the number of cards currently displayed
        employee_count = card_count

        # Update the count label text
        self.employee_count_label.setText(f"Total : {employee_count}")

    def perform_search(self):
        #self.show_personnal_card_form()
        search_text = self.search_field.text().strip().lower()

        self.donnee = self.controller.get_personnel_data()

        personnel_data = []
        
        # Parcourez vos données existantes pour la recherche
        for row in self.donnee:
            badge, nom, categorie, fonction, sous_categorie = row

            if isinstance(badge, int):
                badge = str(badge)
            if isinstance(nom, int):
                nom = str(nom)

            if search_text in badge.lower() or search_text in nom.lower():
                personnel_data.append(row)
        
               
        # Actualisez l'affichage avec les résultats filtrés
        self.refresh_personnel_cards(personnel_data)
        #print(personnel_data)



    def filter_personnel_team(self, index):
        selected_team = self.team_filter.currentText()
        personnel_data = self.controller.get_personnel_by_team(selected_team)
        #self.update_combo_box_items()
        self.refresh_personnel_cards(personnel_data)

    def filter_personnel_SC(self, index):
        selected_SC = self.SC_filter.currentText()
        personnel_data = self.controller.get_personnel_by_SC(selected_SC)
        #self.update_combo_box_items()
        self.refresh_personnel_cards(personnel_data)

    def filter_personnel_Categorie(self, index):
        selected_Categorie = self.Categ_filter.currentText()
        personnel_datas = self.controller.get_personnel_by_Categ(selected_Categorie)
        #self.update_combo_box_items()
        self.refresh_personnel_cards(personnel_datas)

    def update_combo_box_items(self):
        # Clear the existing items
        self.team_filter.clear()
        self.Categ_filter.clear()
        self.SC_filter.clear()
        # Add the initial option
        self.team_filter.addItem("All Teams")
        self.Categ_filter.addItem("All Categ")
        self.SC_filter.addItem("All SC")

        # Fetch and add the updated team names
        equipe_name = self.controller.get_team_names()
        Categ_name = self.controller.get_categ_names()
        SC_name = self.controller.get_SC_names()

        self.team_filter.addItems(equipe_name)
        self.Categ_filter.addItems(Categ_name)
        self.SC_filter.addItems(SC_name)

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
    
        self.cardCount = 0
        #data = self.controller.get_personnel_data or personnel_data
        if data is not None:
            for row_idx, row in enumerate(data):
                badge, nom, categorie, fonction, sous_categorie = row
                card_container = QFrame()
                card_container = Card( badge, nom, categorie, fonction, sous_categorie , self.main_window)
                self.page2_layout.addWidget(card_container, row_idx // 3, row_idx % 3)

                card_container.setStyleSheet(" border-radius: 2px; padding: 5px ; margin :5px ;")

                self.cardCount = self.cardCount + 1

            self.update_employee_count(self.cardCount)

                # Actualisez l'affichage
            self.update()