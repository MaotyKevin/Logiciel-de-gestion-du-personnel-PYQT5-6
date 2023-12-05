import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

from view.team_crud_view import Team_crud
from view.Users_account_crud_view import User_account
from view.SC_view import SC_crud
from view.Admin_account_crud_view import Admin_account
from view.Categorie_view import Categorie_crud

class Admin_crud(QTabWidget):
    def __init__(self , db_path):
        super().__init__()
        db_path = db_path

        
        tab1 = Admin_account(db_path)
        tab2 = User_account(db_path)
        tab3 = Categorie_crud(db_path)
        tab4 = SC_crud(db_path)
        tab5 = Team_crud(db_path)

        self.AdminHeader = "Les administrateurs"
        self.equipeHeader = "Les equipes"
        self.userHeader = "Les utilisateurs"
        self.Categorie_Header = "Categories"
        self.SCHeader = "Sous-Categories"


        # Add tabs to the tab widget
        
        self.addTab(tab1 , self.AdminHeader)
        self.addTab(tab2, self.userHeader)
        self.addTab(tab3 , self.Categorie_Header)
        self.addTab(tab4, self.SCHeader)
        self.addTab(tab5, self.equipeHeader)

        self.setStyleSheet(
            "QTabBar::tab {"
            "    font-weight: bold;"
            "    width: 150px;"
            "}"
            "QTabBar::tab:!selected {"
            "    background-color: #7ed957;"
            "    color: #102429;   "
            "}"
        )

        


        




