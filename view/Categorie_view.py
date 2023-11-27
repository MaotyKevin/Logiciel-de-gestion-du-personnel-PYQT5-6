from PyQt5.QtWidgets import QWidget,QMessageBox,QInputDialog,QHBoxLayout,QPushButton,QFrame,QScrollArea,QGridLayout, QVBoxLayout, QLabel
from controller.team_crud_controller import AdminCrudController
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from view.Categorie_card_view import CategorieCard

class Categorie_crud(QWidget):
    def __init__(self , db_path):
        super().__init__()
        self.db_path = db_path
        self.controller = AdminCrudController(db_path)
        self.C = []
        self.donnee = self.controller.getCategorieData()
        self.initUI()

    def initUI(self):


        self.add_Categorie_button = QPushButton("Nouvelle categorie")
        self.add_Categorie_button.setCursor(Qt.PointingHandCursor)
        self.add_Categorie_button.setStyleSheet("background-color: #102429; color: white; padding: 10px 20px; border: none; border-radius: 5px;")
        self.add_Categorie_button.clicked.connect(self.show_add_C_dialog)
        

        add_C_container = QWidget()
        add_C_layout = QHBoxLayout(add_C_container)
        add_C_layout.addWidget(self.add_Categorie_button)
        add_C_layout.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.page_layout = QGridLayout()
        self.page_layout.setAlignment(QtCore.Qt.AlignTop)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(
            """
            QScrollArea {
                border: 1px solid #CCCCCC;
            }
            
            QScrollBar:vertical {
                border: 1px solid #734001;
                background: #734001;
                width: 12px;
                margin: 0px;
            }
            
            QScrollBar:horizontal {
                border: 1px solid #734001;
                background: #734001;
                height: 12px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #734001;
                min-height: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::handle:horizontal {
                background: #734001;
                min-width: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
            }
            """
        )

        container = QWidget()
        container.setLayout(self.page_layout)
        container.setStyleSheet("background-color: white")

        scroll_area.setWidget(container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(add_C_container)
        main_layout.addWidget(self.populateC())
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def populateC(self):
        data = self.donnee
        if data is not None:
            print(f"C LIST : {data}")
            for row_idx , row in enumerate(data):
                id_categorie , nom_categorie = row 
                card_container = QFrame()
                card_container = CategorieCard(id_categorie , nom_categorie)
                self.page_layout.addWidget(card_container , row_idx // 3, row_idx % 3)
                card_container.setStyleSheet("border-radius:2px ; padding:5px ; margin:5px")
            self.update()

    def show_add_C_dialog(self):
        # Create a dialog to input the new team's name
        CName, ok = QInputDialog.getText(self, "Ajout", "Le nom de la categorie:")
        
        if ok:
            if CName and not CName.isspace():
                # Check if the team name already exists in the database
                if not self.controller.verifyCategorie(CName):
                    # L'équipe n'existe pas encore, vous pouvez l'ajouter
                    self.controller.addCategorie(CName)

                    # Refresh the team list and update the UI
                    self.refresh_C_cards()
                else:
                    # L'équipe existe déjà, affichez un message d'erreur à l'utilisateur
                    QMessageBox.warning(self, "Erreur", "Categorie deja existante.")
            else:
                QMessageBox.warning(self, "Erreur", "Le champ ne peut pas être vide.")     
    
    def refresh_C_cards(self):
        # Clear the current team cards
        for i in reversed(range(self.page_layout.count())):
            widget = self.page_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        # Reload the team data
        self.donnee = self.controller.getCategorieData()
        
        # Populate the UI with the updated team data
        self.populateC()