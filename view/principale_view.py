#view/principale_view.py
from pathlib import Path
import sys
from PyQt5.QtWidgets import QMessageBox,QLineEdit, QApplication,QDesktopWidget,QStackedWidget, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSplitter 
from PyQt5.QtGui import QPalette, QColor 
from PyQt5.QtCore import Qt, QSize , QFile, QTextStream , QRect
from inscription_personnel_view import InscriptionPersonnelForm
from view.personnel_card_view import Personnal_Card
from controller.inscription_personnel_controller import InscriptionPersonnelController
from view.login_view import LoginWindow
from view.employee_detail_view import EmployeeDetailsForm


class CustomHeader(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(80)  
        self.setStyleSheet("background-color: #6495ED;")  
        self.header_label = QLabel("LOGO HERE")
        self.header_label.setStyleSheet("color: white ; font-weight: bolder")
        header_layout = QHBoxLayout()
        header_layout.addWidget(self.header_label)
        self.setLayout(header_layout)


class CustomNavigationBar(QWidget):
    def __init__(self, main_window  ):
        super().__init__()
        self.main_window = main_window  # Référence à la fenêtre principale
        self.setFixedWidth(150)  
        self.navigation_container = QWidget()
        self.navigation_layout = QVBoxLayout(self.navigation_container)
        self.navigation_buttons = []

  
        button = QPushButton(f"Nos employees")
        self.navigation_buttons.append(button)
        self.navigation_layout.addWidget(button)

        button2 = QPushButton(f"Nouveaux personnels")
        self.navigation_buttons.append(button2)
        self.navigation_layout.addWidget(button2)        

        self.logoutButton = QPushButton(F"Logout")
        self.navigation_layout.addWidget(self.logoutButton)

        self.login_view = LoginWindow(db_path , self)
        self.logoutButton.clicked.connect(self.logout)

        self.setLayout(self.navigation_layout)
    
    def logout(self):
        confirmation = QMessageBox.question(self, "Confirmation" , "Etes-vous sur de vouloir vous deconnecter ?",QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.main_window.show_login_view()
            


class MainWindow(QMainWindow):
    def __init__(self , db_path ):
        super().__init__()

        self.setWindowTitle("RH MANAGEMENT - Kevin Copyright")
        self.db_path = db_path
        self.last_displayed_page = None

        
        self.login_view = LoginWindow(db_path , self)
        self.principal_view = None
        self.access = None
        self.show_login_view()

        #self.login_view.show()

        self.setupUI()

    def setupUI(self):    
        # Récupérer la taille de l'écran actuel
        """desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        width, height = screen_rect.width(), screen_rect.height()
        
        # Redimensionner la fenêtre en fonction de la taille de l'écran
        new_size = QSize(int(width*3), int(height*3))
        self.resize(new_size)"""

        # Créez la barre de navigation (1ère partie) en utilisant la classe personnalisée
        self.navigation_bar = CustomNavigationBar(self)  # Passez une référence à MainWindow
        # Utilisez la classe de l'en-tête personnalisée
        self.header = CustomHeader()
        self.header.setStyleSheet("background-color: white")


        # Créez l'espace central (3ème partie)
        self.central_space = QWidget()
        self.central_layout = QVBoxLayout()
        self.search_field = QLineEdit()  # Champ de recherche
        self.central_layout.addWidget(self.search_field)
        self.central_space.setLayout(self.central_layout)

        self.search_field.textChanged.connect(self.perform_search)

        self.search_field.setStyleSheet("Background-color: #FFFFFF;border: 1px solid #CCCCCC; border-radius: 5px; padding: 5px;font-size: 14px;color: #333333;")
        #self.search_field.setFixedWidth(300)
        

        
       

        # Créez un widget pour organiser la barre de navigation et l'espace central horizontalement
        navigation_and_central_layout = QHBoxLayout()
        navigation_and_central_layout.addWidget(self.navigation_bar)
        navigation_and_central_layout.addWidget(self.central_space)

        # Créez un widget pour organiser l'en-tête et le widget précédemment créé verticalement
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.header)
        main_layout.addLayout(navigation_and_central_layout)

        self.container = QWidget()
        self.container.setLayout(main_layout)
        #self.setCentralWidget(self.container)


        # Ajoutez un QStackedWidget pour gérer les pages
        self.stacked_widget = QStackedWidget()
        self.central_layout.addWidget(self.stacked_widget)



        self.personnal_card_form = Personnal_Card(db_path , self)
        self.stacked_widget.addWidget(self.personnal_card_form)

        self.inscri_controller = InscriptionPersonnelController()
        self.inscription_form = InscriptionPersonnelForm(db_path , self.inscri_controller) 
        self.inscri_controller.view = self.inscription_form      
        self.stacked_widget.addWidget(self.inscription_form)


        self.navigation_bar.navigation_buttons[0].clicked.connect(self.show_personnal_card_form)
        self.navigation_bar.navigation_buttons[1].clicked.connect(self.show_inscription_page)
        self.show_personnal_card_form()

    """   def return_to_last_displayed_page(self):
        
        if self.last_displayed_page:
            if isinstance(self.last_displayed_page, EmployeeDetailsForm):
                self.setupUI()
                # self.show_personnal_card_form()  # Return to the list of cards
            else:
                self.stacked_widget.setCurrentWidget(self.last_displayed_page)
            if self.last_displayed_page == self.personnal_card_form:
                self.personnal_card_form.refresh_personnel_cards()
               """ 
    def show_employee_details_view(self, employee_details_form):
        # Replace the current view with the EmployeeDetailsForm
        if self.last_displayed_page:
            self.last_displayed_page.hide()
        self.setCentralWidget(employee_details_form)
        self.last_displayed_page = employee_details_form

    def show_principal_view(self):
        #self.login_view.hide()
        self.setupUI()
        self.setCentralWidget(self.container)

    def show_login_view(self):
        self.login_view = LoginWindow(db_path , self)
        self.setCentralWidget(self.login_view)
        self.login_view.show()

    def perform_search(self):
        #self.show_personnal_card_form()
        search_text = self.search_field.text().strip().lower()
        print(f"Reception search text: {search_text} , bouton fonctionnel")
        print(f"Données existantes : {self.personnal_card_form.personnel_data}")

        self.personnal_card_form.donnee = self.personnal_card_form.controller.get_personnel_data()

        self.donnee = self.personnal_card_form.donnee
        personnel_data = []
        
        # Parcourez vos données existantes pour la recherche
        for row in self.donnee:
            badge, nom, categorie, fonction, sous_categorie = row
            if search_text in badge.lower() or search_text in nom.lower():
                personnel_data.append(row)
        
               
        # Actualisez l'affichage avec les résultats filtrés
        self.personnal_card_form.refresh_personnel_cards(personnel_data)
        #print(personnel_data)

    def return_to_last_displayed_page(self , employee_details_form):
        print("return last displayed called")
        if self.last_displayed_page:
            print("last displayed page condition ok")
            self.show_principal_view()
            self.stacked_widget.setCurrentWidget(self.last_displayed_page)

            # Si la dernière page affichée est la page des cartes du personnel, actualisez les cartes
            if self.last_displayed_page == self.personnal_card_form:
                self.personnal_card_form.refresh_personnel_cards()
            if self.last_displayed_page == employee_details_form:
                self.setupUI()
        

    def show_inscription_page(self):
        self.stacked_widget.setCurrentWidget(self.inscription_form)
        self.inscription_form.updateButtonVisibility()

    def show_personnal_card_form(self):
        self.last_displayed_page = self.personnal_card_form
        self.stacked_widget.setCurrentWidget(self.personnal_card_form)
        self.personnal_card_form.refresh_personnel_cards()
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    db_path = 'data/my_database.sqlite'
    window = MainWindow(db_path)

    window.showMaximized() 
    
    sys.exit(app.exec_())