from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QWidget,QInputDialog,QPushButton,QHBoxLayout,QFrame,QScrollArea,QGridLayout, QVBoxLayout, QLabel
from controller.team_crud_controller import AdminCrudController
from PyQt5 import QtCore 
from PyQt5.QtCore import Qt
from view.Admin_card_view import AdminAccountCard

class Admin_account(QWidget):
    def __init__(self , db_path):
        super().__init__()
        self.db_path = db_path
        self.controller = AdminCrudController(db_path)
        self.user = []
        self.donnee = self.controller.getAdminData()
        self.initUI()

    def initUI(self):

        self.add_user_button = QPushButton("Nouvel admin")
        self.add_user_button.setStyleSheet("background-color: #102429; color: white; padding: 10px 20px; border: none; border-radius: 5px;")
        self.add_user_button.clicked.connect(self.show_add_user_dialog)
        

        add_user_container = QWidget()
        add_user_layout = QHBoxLayout(add_user_container)
        add_user_layout.addWidget(self.add_user_button)
        add_user_layout.setAlignment(Qt.AlignRight | Qt.AlignTop)

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
        main_layout.addWidget(add_user_container)
        main_layout.addWidget(self.populateAdmin())
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def populateAdmin(self):
        data = self.donnee
        if data is not None:
            for row_idx , row in enumerate(data):
                id_user , username , password = row 
                card_container = QFrame()
                card_container = AdminAccountCard(id_user , username , password)
                self.page_layout.addWidget(card_container , row_idx // 3, row_idx % 3)
                card_container.setStyleSheet("border-radius:2px ; padding:5px ; margin:5px")
            self.update()

    def show_add_user_dialog(self):
        # Create a custom dialog to input the new username and password
        dialog = AddUserDialog(self)
        
        # Show the dialog and wait for the user's input
        if dialog.exec_() == QDialog.Accepted:
            # Get the entered username and password from the dialog
            username = dialog.get_username()
            password = dialog.get_password()
            
            if not self.controller.verifyAdminName(username) or not self.controller.verifyAdminPassword(password):
                # L'équipe n'existe pas encore, vous pouvez l'ajouter
                self.controller.add_Admin(username , password)

                # Refresh the team list and update the UI
                self.refresh_user_cards()
            else:
                # L'équipe existe déjà, affichez un message d'erreur à l'utilisateur
                QMessageBox.warning(self, "Erreur", "Pseudo ou mot de passe deja existant.")

    def refresh_user_cards(self):
        # Clear the current team cards
        for i in reversed(range(self.page_layout.count())):
            widget = self.page_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        # Reload the team data
        self.donnee = self.controller.getAdminData()
        
        # Populate the UI with the updated team data
        self.populateAdmin()


class AddUserDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nouvel admin")
        
        self.username_label = QLabel("Pseudo:")
        self.username_input = QLineEdit(self)
        
        self.password_label = QLabel("Mot de passe :")
        self.password_input = QLineEdit(self)
        
        self.add_button = QPushButton("Creer")
        self.add_button.clicked.connect(self.check_and_accept)
        
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.add_button)
        
        self.setLayout(layout)
    
    def get_username(self):
        return self.username_input.text()
    
    def get_password(self):
        return self.password_input.text()
    
    def check_and_accept(self):
        username = self.get_username()
        password = self.get_password()
        
        if not username or not password:
            QMessageBox.warning(self, "Attention", "Tous les champs a completer.")
        else:
            self.accept()