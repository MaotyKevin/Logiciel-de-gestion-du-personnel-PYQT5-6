#view/step_three.py

import sys
import os
from PyQt5.QtWidgets import QApplication,QScrollArea, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QStackedWidget, QDateEdit, QMessageBox , QHBoxLayout
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
        self.fonction_edit.setPlaceholderText("Fonction")
        self.fonction_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #102429; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.deuxieme_fonction_edit = QLineEdit()
        self.deuxieme_fonction_edit.setPlaceholderText("2e fonction")
        self.deuxieme_fonction_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #102429; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.date_debut_edit = QDateEdit(QDate.currentDate())
        self.date_debut_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_debut_edit.setCalendarPopup(True)
        self.date_debut_edit.setStyleSheet("""
            QDateEdit {
                border: 1px solid #CCCCCC; 
                color:white;
                border-radius: 5px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #102429; /* White background */
            }
        
            QDateEdit::down-arrow {background-color: #7ed957;}
                                         
            QCalendarWidget QWidget {
                background-color: black;
                alternate-background-color: black;
                color:white;
            }

        """)

        self.date_fin_edit = QDateEdit(QDate.currentDate())
        self.date_fin_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_fin_edit.setCalendarPopup(True)
        self.date_fin_edit.setStyleSheet("""
            QDateEdit {
                border: 1px solid #CCCCCC; 
                color:white;
                border-radius: 5px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #102429; /* White background */
            }
        
            QDateEdit::down-arrow {background-color: #7ed957;}
                                         
            QCalendarWidget QWidget {
                background-color: black;
                alternate-background-color: black;
                color:white;
            }

        """)
        

        self.cause_depart_edit = QLineEdit()
        self.cause_depart_edit.setPlaceholderText("Cause de depart")
        self.cause_depart_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #102429; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.date_equipement_edit = QDateEdit(QDate.currentDate())
        self.date_equipement_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_equipement_edit.setCalendarPopup(True)
        self.date_equipement_edit.setStyleSheet("""
            QDateEdit {
                border: 1px solid #CCCCCC; 
                color:white;
                border-radius: 5px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #102429; /* White background */
            }
        
            QDateEdit::down-arrow {background-color: #7ed957;}
                                         
            QCalendarWidget QWidget {
                background-color: black;
                alternate-background-color: black;
                color:white;
            }

        """)

        self.casque_edit = QLineEdit()
        self.casque_edit.setPlaceholderText("Casque")
        self.casque_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #102429; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.haut_edit = QLineEdit()
        self.haut_edit.setPlaceholderText("Haut")
        self.haut_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #102429; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.lunette_edit = QLineEdit()
        self.lunette_edit.setPlaceholderText("Lunette")
        self.lunette_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #102429; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.chaussure_edit = QLineEdit()
        self.chaussure_edit.setPlaceholderText("Chaussure")
        self.chaussure_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #102429; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)


        
      
        self.enregistrer_button = QPushButton("Enregistrer")
        self.enregistrer_button.setCursor(Qt.PointingHandCursor)
        self.enregistrer_button.setStyleSheet("background-color: #7ed957; color: #102429; padding: 10px 20px; border: none; border-radius: 5px; font-weight:bold;")



        layout.addWidget(QLabel("Fonction:"))
        layout.addWidget(self.fonction_edit)
        layout.addWidget(QLabel("Deuxième fonction:"))
        layout.addWidget(self.deuxieme_fonction_edit)
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
                border: 1px solid white;
                background: #102429;
                width: 12px;
                margin: 0px;
            }
            
            QScrollBar:horizontal {
                border: 1px solid white;
                background: #102429;
                height: 12px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #102429;
                min-height: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::handle:horizontal {
                background: #102429;
                min-width: 20px;
                border-radius: 6px;
            }
            
            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
            }
            """
        )