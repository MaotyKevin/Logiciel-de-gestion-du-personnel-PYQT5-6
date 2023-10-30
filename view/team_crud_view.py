from PyQt5.QtWidgets import  QMessageBox,  QWidget,QInputDialog,QPushButton,QHBoxLayout,QFrame,QScrollArea,QGridLayout, QVBoxLayout, QLabel
from controller.team_crud_controller import AdminCrudController
from PyQt5 import QtCore 
from PyQt5.QtCore import Qt

from view.card_team_view import TeamCard

class Team_crud(QWidget):
    def __init__(self , db_path):
        super().__init__()
        self.db_path = db_path
        self.controller = AdminCrudController(db_path)
        self.team = []
        self.donnee = self.controller.getTeamData()
        self.initUI()

    def initUI(self):

        self.add_team_button = QPushButton("Nouvelle equipe")
        self.add_team_button.setStyleSheet("background-color: #007BFF; color: white; padding: 10px 20px; border: none; border-radius: 5px;")
        self.add_team_button.clicked.connect(self.show_add_team_dialog)
        

        add_team_container = QWidget()
        add_team_layout = QHBoxLayout(add_team_container)
        add_team_layout.addWidget(self.add_team_button)
        add_team_layout.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.page_layout = QGridLayout()
        self.page_layout.setAlignment(QtCore.Qt.AlignTop)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        container.setLayout(self.page_layout)
        container.setStyleSheet("background-color: white")

        scroll_area.setWidget(container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(add_team_container)
        main_layout.addWidget(self.populateTeam())
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
        
        

    def populateTeam(self):
        data = self.donnee
        if data is not None:
            for row_idx , row in enumerate(data):
                id_equipe , nom_equipe = row 
                card_container = QFrame()
                card_container = TeamCard(id_equipe , nom_equipe)
                self.page_layout.addWidget(card_container , row_idx // 3, row_idx % 3)
                card_container.setStyleSheet("border-radius:2px ; padding:5px ; margin:5px")
            self.update()

    def show_add_team_dialog(self):
        # Create a dialog to input the new team's name
        team_name, ok = QInputDialog.getText(self, "Ajout d'Equipe", "Le nom de l'equipe :")
        
        if ok:
            # Check if the team name is empty or consists of only whitespace
            if team_name and not team_name.isspace():
                # Check if the team name already exists in the database
                if not self.controller.verifyTeam(team_name):
                    # L'équipe n'existe pas encore, vous pouvez l'ajouter
                    self.controller.add_team(team_name)

                    # Refresh the team list and update the UI
                    self.refresh_team_cards()
                else:
                    # L'équipe existe déjà, affichez un message d'erreur à l'utilisateur
                    QMessageBox.warning(self, "Erreur", "Équipe existante.")
            else:
                # Le champ équipe est vide ou ne contient que des espaces, affichez un message d'erreur
                QMessageBox.warning(self, "Erreur", "Le champ équipe ne peut pas être vide.")

    def refresh_team_cards(self):
        # Clear the current team cards
        for i in reversed(range(self.page_layout.count())):
            widget = self.page_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        # Reload the team data
        self.donnee = self.controller.getTeamData()
        
        # Populate the UI with the updated team data
        self.populateTeam()