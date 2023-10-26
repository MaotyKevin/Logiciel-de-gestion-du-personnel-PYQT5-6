from PyQt5.QtWidgets import QWidget,QInputDialog,QHBoxLayout,QPushButton,QFrame,QScrollArea,QGridLayout, QVBoxLayout, QLabel
from controller.team_crud_controller import AdminCrudController
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from view.SC_card_view import SCCard

class SC_crud(QWidget):
    def __init__(self , db_path):
        super().__init__()
        self.db_path = db_path
        self.controller = AdminCrudController(db_path)
        self.SC = []
        self.donnee = self.controller.getSCData()
        self.initUI()

    def initUI(self):


        self.add_SC_button = QPushButton("Add SC")
        self.add_SC_button.setStyleSheet("background-color: #007BFF; color: white; padding: 10px 20px; border: none; border-radius: 5px;")
        self.add_SC_button.clicked.connect(self.show_add_SC_dialog)
        

        add_SC_container = QWidget()
        add_SC_layout = QHBoxLayout(add_SC_container)
        add_SC_layout.addWidget(self.add_SC_button)
        add_SC_layout.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.page_layout = QGridLayout()
        self.page_layout.setAlignment(QtCore.Qt.AlignTop)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        container.setLayout(self.page_layout)
        container.setStyleSheet("background-color: white")

        scroll_area.setWidget(container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(add_SC_container)
        main_layout.addWidget(self.populateSC())
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def populateSC(self):
        data = self.donnee
        if data is not None:
            print(f"SC LIST : {data}")
            for row_idx , row in enumerate(data):
                id_sousCategorie , sousCategorie = row 
                card_container = QFrame()
                card_container = SCCard(id_sousCategorie , sousCategorie)
                self.page_layout.addWidget(card_container , row_idx // 3, row_idx % 3)
                card_container.setStyleSheet("border-radius:2px ; padding:5px ; margin:5px")
            self.update()

    def show_add_SC_dialog(self):
        # Create a dialog to input the new team's name
        SCName, ok = QInputDialog.getText(self, "Add SC", "Enter the SC's name:")
        
        if ok:
            # Call your controller's method to add the new team
            self.controller.addSC(SCName)
            
            # Refresh the team list and update the UI
            self.refresh_SC_cards()

    def refresh_SC_cards(self):
        # Clear the current team cards
        for i in reversed(range(self.page_layout.count())):
            widget = self.page_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        # Reload the team data
        self.donnee = self.controller.getSCData()
        
        # Populate the UI with the updated team data
        self.populateSC()