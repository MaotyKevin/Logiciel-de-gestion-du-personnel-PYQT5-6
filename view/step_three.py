#view/step_three.py

import sys
import os
from PyQt5.QtWidgets import QApplication,QScrollArea, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QStackedWidget, QDateEdit, QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter
from PyQt5.QtCore import Qt, QDate 

class StepTree(QScrollArea):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        content_widget = QWidget()
        layout = QVBoxLayout()
        content_widget.setLayout(layout)
        # Add the remaining input fields here

        self.fonction_edit = QLineEdit()
        self.deuxieme_fonction_edit = QLineEdit()
        self.categorie_edit = QLineEdit()

        self.date_debut_edit = QDateEdit(QDate.currentDate())
        #self.date_debut_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_debut_edit.setCalendarPopup(True)

        self.date_fin_edit = QDateEdit(QDate.currentDate())
        #self.date_fin_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_fin_edit.setCalendarPopup(True)
        

        self.cause_depart_edit = QLineEdit()

        self.date_equipement_edit = QDateEdit(QDate.currentDate())
        #self.date_equipement_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_equipement_edit.setCalendarPopup(True)

        self.casque_edit = QLineEdit()
        self.haut_edit = QLineEdit()
        self.lunette_edit = QLineEdit()
        self.chaussure_edit = QLineEdit()

      
        self.enregistrer_button = QPushButton("Enregistrer")

        layout.addWidget(QLabel("Fonction:"))
        layout.addWidget(self.fonction_edit)
        layout.addWidget(QLabel("Deuxième fonction:"))
        layout.addWidget(self.deuxieme_fonction_edit)
        layout.addWidget(QLabel("Catégorie:"))
        layout.addWidget(self.categorie_edit)
        layout.addWidget(QLabel("Date début:"))
        layout.addWidget(self.date_debut_edit)
        layout.addWidget(QLabel("Date fin:"))
        layout.addWidget(self.date_fin_edit)
        layout.addWidget(QLabel("Cause départ:"))
        layout.addWidget(self.cause_depart_edit)
        layout.addWidget(QLabel("Date équipement:"))
        layout.addWidget(self.date_equipement_edit)
        layout.addWidget(QLabel("Casque:"))
        layout.addWidget(self.casque_edit)
        layout.addWidget(QLabel("Haut:"))
        layout.addWidget(self.haut_edit)
        layout.addWidget(QLabel("Lunette:"))
        layout.addWidget(self.lunette_edit)
        layout.addWidget(QLabel("Chaussure:"))
        layout.addWidget(self.chaussure_edit)
        layout.addWidget(self.enregistrer_button)

        # ...
        self.setWidget(content_widget)
        self.setWidgetResizable(True)

        self.setStyleSheet(
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