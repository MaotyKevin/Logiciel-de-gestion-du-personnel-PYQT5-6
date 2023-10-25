import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

from view.team_crud_view import Team_crud
from view.Users_account_crud_view import User_account

class Admin_crud(QTabWidget):
    def __init__(self , db_path):
        super().__init__()
        db_path = db_path

        # Create tabs
        tab1 = Team_crud(db_path)
        tab2 = User_account()
        

        # Add tabs to the tab widget
        self.addTab(tab1, "Les equipes")
        self.addTab(tab2, "Les comptes")
        


        




