#view/principale_view.py
from pathlib import Path
import sys , os
from PyQt5.QtWidgets import QMessageBox,QLineEdit, QApplication,QDesktopWidget,QStackedWidget, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSplitter 
from PyQt5.QtGui import QPalette, QColor  , QIcon
from PyQt5.QtCore import Qt, QSize , QFile, QTextStream , QRect
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from view.inscription_personnel_view import InscriptionPersonnelForm
from view.personnel_card_view import Personnal_Card
from controller.inscription_personnel_controller import InscriptionPersonnelController
from view.login_view import LoginWindow
from view.employee_detail_view import EmployeeDetailsForm
from view.admin_crud_view import Admin_crud
from view.sender_view import MessageSender
from view.receiver_view import MessageReceiver

class CustomHeader(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(80)

     

        self.header_label = QLabel()
        self.header_label.setStyleSheet("color: white; font-weight: bolder")



        self.message_button = QPushButton("  CHAT")
        self.message_button.setIcon(QIcon("assets\pic\chat.svg"))
        self.message_button.setStyleSheet("background-color: white; color: black; padding: 10px 20px; border: none; border-radius: 5px;")

        header_layout = QHBoxLayout()  # Horizontal layout for the header content
        header_layout.addWidget(self.header_label)
        header_layout.addStretch(1)  # Add a stretch to push the message button to the right
        header_layout.addWidget(self.message_button)

        centre = QWidget()
        centre.setLayout(header_layout)
        centre.setStyleSheet("background-color: #734001; border-radius: 4px;")
        layout = QVBoxLayout()  # Vertical layout for top alignment
        layout.addWidget(centre)
        self.setLayout(layout)

class CustomNavigationBar(QWidget):
    def __init__(self, main_window  , db_path):
        super().__init__()
        self.main_window = main_window  # Référence à la fenêtre principale
        self.setFixedWidth(150)  
        #self.navigation_container = QWidget()
        #self.navigation_container.setObjectName("nav-container")
        
        self.navigation_layout = QVBoxLayout() #(self.navigation_container)
        
        self.navigation_buttons = []

        self.db_path = db_path

        
        button = QPushButton("  Effectif")
        button.setToolTip("Effectif")
        self.navigation_buttons.append(button)
        self.navigation_layout.addWidget(button)
        button.setIcon(QIcon("assets\pic\effectif.png"))
        button.setStyleSheet("border : none;background-color : white ;padding : 10px 20px ;color: #161c2a;border-radius: 5px;")

        button1 = QPushButton("  Admin")
        button.setToolTip("Admin")
        self.navigation_buttons.append(button1)
        self.navigation_layout.addWidget(button1)
        button1.setIcon(QIcon("assets/pic/admin.png"))
        button1.setStyleSheet("border : none;background-color : white;padding : 10px 20px ;color: #161c2a;border-radius: 5px;")

        button2 = QPushButton(f"  Recruter")
        self.navigation_buttons.append(button2)
        self.navigation_layout.addWidget(button2)
        button2.setIcon(QIcon("assets/pic/recruter.png"))  
        button2.setStyleSheet("border : none;background-color : white ;padding : 10px 20px ;color: #161c2a;border-radius: 5px;")
      

        self.logoutButton = QPushButton(F"  Logout")
        self.logoutButton.setIcon(QIcon("assets\pic\logout.png"))
        self.logoutButton.setStyleSheet("border : none;background-color : white;padding : 10px 20px ;color: #161c2a;border-radius: 5px;")
        self.navigation_layout.addWidget(self.logoutButton)

        self.login_view = LoginWindow(self.db_path , self)
        self.logoutButton.clicked.connect(self.logout)

        centre = QWidget()
        centre.setLayout(self.navigation_layout)
        centre.setStyleSheet("""
                            background-color: #734001; 
                            border : 1px solid white;
                            border-radius:5px;
                            QPushButton {
                                border : none;
                                background-color : white;
                                padding : 10px 20px ;
                                color: black;
                                border-radius: 5px;
                            }

                            QPushButton::hover {
                                padding : 5px 15px;
                                border: 1px solid #161c2a;
                                background-color:white;
                                color: black;
                            }
                             
                             """)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(centre)
        
        


    
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
        self.setStyleSheet("background-color: white;")

    def setupUI(self):    

        self.navigation_bar = CustomNavigationBar( self, self.db_path)  # Passez une référence à MainWindow
        
        """self.navigation_bar.setStyleSheet(
            
            QPushButton {
                border : none;
                background-color : black;
                padding : 10px 20px ;
                color: white;
                border-radius: 5px;
            }

            QPushButton::hover {
                padding : 5px 15px;
                background-color:white;
                color: black;
            }
                                          
            
          
             
        )"""
     
        self.header = CustomHeader()
        self.header.setStyleSheet("background-color: white")

        self.central_space = QWidget()
        self.central_layout = QVBoxLayout()
        
        #self.central_layout.addWidget(self.search_field)
        self.central_space.setLayout(self.central_layout)




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
        self.stacked_widget.setStyleSheet("background-color: white;")
        self.central_layout.addWidget(self.stacked_widget)

        self.send = MessageSender()
        self.stacked_widget.addWidget(self.send)

        self.admin_crud = Admin_crud(self.db_path)
        self.stacked_widget.addWidget(self.admin_crud)

        self.personnal_card_form = Personnal_Card(self.db_path , self)
        self.stacked_widget.addWidget(self.personnal_card_form)

        self.inscri_controller = InscriptionPersonnelController()
        self.inscription_form = InscriptionPersonnelForm(self.db_path , self.inscri_controller) 
        self.inscri_controller.view = self.inscription_form      
        self.stacked_widget.addWidget(self.inscription_form)

        self.header.message_button.clicked.connect(self.show_sender)

        self.navigation_bar.navigation_buttons[0].clicked.connect(self.show_personnal_card_form)
        self.navigation_bar.navigation_buttons[1].clicked.connect(self.show_admin_crud)
        self.navigation_bar.navigation_buttons[2].clicked.connect(self.show_inscription_page)

        self.show_personnal_card_form()

    def show_employee_details_view(self, employee_details_form):
        # Replace the current view with the EmployeeDetailsForm
        #if self.last_displayed_page:
            #self.last_displayed_page.hide()
        self.stacked_widget.addWidget(employee_details_form)
        self.stacked_widget.setCurrentWidget(employee_details_form)
        self.last_displayed_page = employee_details_form

    def show_principal_view(self):
        self.setupUI()
        self.setCentralWidget(self.container)

    def show_client_message(self , usernames ):
        self.client_message = MessageReceiver(self , usernames)
        self.setCentralWidget(self.client_message)
        self.client_message.show()

    def show_login_view(self):
        self.login_view = LoginWindow(self.db_path , self)
        self.setCentralWidget(self.login_view)
        self.login_view.show()

    def return_to_last_displayed_page(self , employee_details_form):
        if self.last_displayed_page:
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
        self.personnal_card_form.update_combo_box_items()
    
    def show_admin_crud(self):
        self.stacked_widget.setCurrentWidget(self.admin_crud)

    def show_sender(self):
        self.stacked_widget.setCurrentWidget(self.send)

    def setLoggedUserInfo(self, username):
        print(f"TESTTTTT : {username}")
        self.logged_username = username
        print(f"LOGGED AS {self.logged_username}")
     
        # You can also perform additional actions, like updating the UI with the user's info
        self.updateUserInfoInUI(self.logged_username)

    def updateUserInfoInUI(self, username):
        # Update the UI elements with the user's info as needed
        # For example, you can set the header label text with the username
        self.header.header_label.setText(f"Logged in as {username}")
        print(f"Header : {username}")