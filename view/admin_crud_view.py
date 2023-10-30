import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

from view.team_crud_view import Team_crud
from view.Users_account_crud_view import User_account
from view.SC_view import SC_crud

class Admin_crud(QTabWidget):
    def __init__(self , db_path):
        super().__init__()
        db_path = db_path


        tab1 = User_account(db_path)
        tab2 = SC_crud(db_path)
        tab3 = Team_crud(db_path)
        
        self.equipeHeader = "Les equipes"
        self.userHeader = "Les comptes"
        self.SCHeader = "Sous-Categorie"
        

        # Add tabs to the tab widget
        self.addTab(tab1, self.userHeader)
        self.addTab(tab2 , self.SCHeader)
        self.addTab(tab3, self.equipeHeader)

        self.setStyleSheet(
            "QTabBar::tab {"
            "    font-weight: bold;"
            "    width: 150px;"
            "}"
            "QTabBar::tab:!selected {"
            "    background-color: #734001;"
            "    color: white;   "
            "}"
        )

        


        




