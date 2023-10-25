from PyQt5.QtWidgets import QWidget,QFrame,QScrollArea,QGridLayout, QVBoxLayout, QLabel
from controller.team_crud_controller import AdminCrudController
from PyQt5 import QtCore

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
        self.page_layout = QGridLayout()
        self.page_layout.setAlignment(QtCore.Qt.AlignTop)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        container.setLayout(self.page_layout)
        container.setStyleSheet("background-color: white")

        scroll_area.setWidget(container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.populateTeam())
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def populateTeam(self):
        data = self.donnee
        if data is not None:
            print(f"EQUIPE LIST : {data}")
            for row_idx , row in enumerate(data):
                id_equipe , nom_equipe = row 
                card_container = QFrame()
                card_container = TeamCard(id_equipe , nom_equipe)
                self.page_layout.addWidget(card_container , row_idx // 3, row_idx % 3)
                card_container.setStyleSheet("border-radius:2px ; padding:5px ; margin:5px")
            self.update()