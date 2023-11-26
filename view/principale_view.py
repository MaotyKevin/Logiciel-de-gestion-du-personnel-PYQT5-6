#view/principale_view.py
from pathlib import Path
import sys , os
from PyQt5.QtWidgets import QMessageBox,QLineEdit, QApplication,QDesktopWidget,QStackedWidget, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSplitter  , QMenu ,QAction
from PyQt5.QtGui import QPalette, QColor  , QIcon
from PyQt5.QtCore import Qt, QSize , QFile, QTextStream , QRect
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from view.inscription_personnel_view import InscriptionPersonnelForm
from view.personnel_card_view import Personnal_Card
from controller.inscription_personnel_controller import InscriptionPersonnelController
from controller.chat_controller import ChatController
from view.login_view import LoginWindow
from view.employee_detail_view import EmployeeDetailsForm
from view.admin_crud_view import Admin_crud
from view.sender_view import MessageSender
from view.receiver_view import MessageReceiver



class CustomHeader(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(80)

        self.toggle_button = QPushButton("FANAHISOA ENTREPRISE")
        self.toggle_button.setToolTip("Afficher/reduire la barre de navigation")
        self.toggle_button.setCursor(Qt.PointingHandCursor)
        self.toggle_button.setStyleSheet("border: none; background-color: transparent; color: white; padding: 10px 20px; border-radius: 5px;font-weight: bolder;")


        self.header_label = QLabel()
        self.header_label.setStyleSheet("color: white; font-weight: bolder")

        self.profile_button = QPushButton()
        self.profile_button.setIcon(QIcon("assets\pic\profile.svg"))
        self.profile_button.setCursor(Qt.PointingHandCursor)
        self.profile_button.setIconSize(QSize(40, 40))  # Set the size of the circular icon
        self.profile_button.setFixedSize(50, 50)  # Set the fixed size for the circular button
        self.profile_button.setStyleSheet("border: none; background-color: transparent;")
        self.profile_button.clicked.connect(self.show_profile_menu)

        self.header_layout = QHBoxLayout()  # Horizontal layout for the header content
        self.header_layout.addWidget(self.toggle_button, alignment=Qt.AlignLeft)
        self.header_layout.addStretch(1)  # Add a stretch to push the message button to the right
        self.header_layout.addWidget(self.profile_button)
        #self.header_layout.addWidget(self.header_label)

        centre = QWidget()
        centre.setLayout(self.header_layout)
        centre.setStyleSheet("background-color: #102429; border-radius: 4px;")
        layout = QVBoxLayout()  # Vertical layout for top alignment
        layout.addWidget(centre)
        self.setLayout(layout)

    def show_profile_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet("background-color: black;color:white;font-weight:bold;")
        
        # Add actions for user information
        user_name_action = QAction(f"Utilisateur actuel : {self.activeName}")

        menu.addAction(user_name_action)
        
        menu_pos = self.profile_button.mapToGlobal(self.profile_button.rect().bottomLeft())
        
        # Add any other actions or options you want in the profile dropdown

        menu.exec_(menu_pos)

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
        button.setToolTip("Gerer le personnel")
        button.setCursor(Qt.PointingHandCursor)
        self.navigation_buttons.append(button)
        self.navigation_layout.addWidget(button)
        button.setIcon(QIcon("assets\pic\effectif.png"))
        button.setStyleSheet("border : none;background-color : white ;padding : 10px 20px ;color: #161c2a;border-radius: 5px;")

        self.navigation_layout.addSpacing(10)

        button1 = QPushButton("  Admin")
        button1.setToolTip("Gestion des comptes , infrastructures....")
        button1.setCursor(Qt.PointingHandCursor)
        self.navigation_buttons.append(button1)
        self.navigation_layout.addWidget(button1)
        button1.setIcon(QIcon("assets/pic/admin.png"))
        button1.setStyleSheet("border : none;background-color : white;padding : 10px 20px ;color: #161c2a;border-radius: 5px;")

        self.navigation_layout.addSpacing(10)

        button2 = QPushButton(f"  Recruter")
        button2.setToolTip("Ajouter un nouvel employee")
        button2.setCursor(Qt.PointingHandCursor)
        self.navigation_buttons.append(button2)
        self.navigation_layout.addWidget(button2)
        button2.setIcon(QIcon("assets/pic/recruter.png"))  
        button2.setStyleSheet("border : none;background-color : white ;padding : 10px 20px ;color: #161c2a;border-radius: 5px;")

        self.navigation_layout.addSpacing(10)

        self.message_button = QPushButton("  Message")
        self.message_button.setIcon(QIcon("assets\pic\chat.svg"))
        self.message_button.setToolTip("Envoyer un message a un utilisateur")
        self.message_button.setCursor(Qt.PointingHandCursor)
        self.message_button.setStyleSheet("background-color: white; color: black; padding: 10px 20px; border: none; border-radius: 5px;")
        self.navigation_buttons.append(self.message_button)
        self.navigation_layout.addWidget(self.message_button)

        self.navigation_layout.addStretch(1)

        self.logoutButton = QPushButton(F"  Deconnexion")
        self.logoutButton.setToolTip("Se deconnecter du compte")
        self.logoutButton.setCursor(Qt.PointingHandCursor)
        self.logoutButton.setIcon(QIcon("assets\pic\logout.png"))
        self.logoutButton.setStyleSheet("border : none;background-color : white;padding : 10px 20px ;color: #161c2a;border-radius: 5px;")
        self.navigation_layout.addWidget(self.logoutButton)

        self.login_view = LoginWindow(self.db_path , self)
        self.logoutButton.clicked.connect(self.logout)

        centre = QWidget()
        centre.setLayout(self.navigation_layout)
        centre.setStyleSheet("""
                            background-color: #102429; 
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
        
        self.setWindowTitle("Gestion de personnel - FANAHISOA & Maoty Copyright")
        self.db_path = db_path
        self.last_displayed_page = None
        self.logged_username = None
        
        self.login_view = LoginWindow(db_path , self)
        self.principal_view = None
        self.access = None
        self.show_login_view()

        #self.login_view.show()

        self.setupUI()
        self.setStyleSheet("background-color: white;")

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
        self.header.activeName = username
        print(f"Header : {username}")

     
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




        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.navigation_bar)
        self.splitter.addWidget(self.central_space)
        self.splitter.setCollapsible(0, True)  # Allow collapsing the CustomNavigationBar

        # Créez un widget pour organiser l'en-tête et le widget précédemment créé verticalement
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.header)
        main_layout.addWidget(self.splitter)

        self.container = QWidget()
        self.container.setLayout(main_layout)
        #self.setCentralWidget(self.container)

    
        # Ajoutez un QStackedWidget pour gérer les pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet("background-color: white;")
        self.central_layout.addWidget(self.stacked_widget)

        self.controllerChat = ChatController(self.db_path)
        self.sampleUsersName = self.controllerChat.sampleUserName()
      
        self.send = MessageSender(  self.db_path , self.logged_username , self.sampleUsersName)
        self.stacked_widget.addWidget(self.send)

        self.admin_crud = Admin_crud(self.db_path)
        self.stacked_widget.addWidget(self.admin_crud)

        self.personnal_card_form = Personnal_Card(self.db_path , self)
        self.stacked_widget.addWidget(self.personnal_card_form)

        self.inscri_controller = InscriptionPersonnelController()
        self.inscription_form = InscriptionPersonnelForm(self.db_path , self.inscri_controller) 
        self.inscri_controller.view = self.inscription_form      
        self.stacked_widget.addWidget(self.inscription_form)

        self.header.toggle_button.clicked.connect(self.toggle_navigation_bar)

        self.navigation_bar.navigation_buttons[0].clicked.connect(self.show_personnal_card_form)
        self.navigation_bar.navigation_buttons[1].clicked.connect(self.show_admin_crud)
        self.navigation_bar.navigation_buttons[2].clicked.connect(self.show_inscription_page)
        self.navigation_bar.navigation_buttons[3].clicked.connect(self.show_sender)

        self.show_personnal_card_form()

    def toggle_navigation_bar(self):
        # Toggle the visibility of the CustomNavigationBar
        self.navigation_bar.setVisible(not self.navigation_bar.isVisible())

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

    def show_client_message(self , id , usernames ):
        self.client_message = MessageReceiver(self , id , usernames)
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
        self.inscription_form.remplir_liste_equipe()
        self.inscription_form.remplir_liste_sous_categorie()
        self.inscription_form.updateButtonVisibility()

    def show_personnal_card_form(self):
        self.last_displayed_page = self.personnal_card_form
        self.stacked_widget.setCurrentWidget(self.personnal_card_form)
        self.personnal_card_form.refresh_personnel_cards()
        self.personnal_card_form.update_combo_box_items()
    
    def show_admin_crud(self):
        self.stacked_widget.setCurrentWidget(self.admin_crud)

    def show_sender(self):
        self.userMaj = self.controllerChat.sampleUserName()
        self.send.updateData(self.userMaj)
        self.stacked_widget.setCurrentWidget(self.send)


