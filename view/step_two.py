#view/step_two.py

import sys
import os
from PyQt5.QtWidgets import QApplication,QScrollArea, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QStackedWidget, QDateEdit, QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter
from PyQt5.QtCore import Qt, QDate 

class StepTwo(QScrollArea):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        content_widget = QWidget()
        layout = QVBoxLayout()
        content_widget.setLayout(layout)

        
        # Add the remaining input fields here
        self.du_edit = QDateEdit(QDate.currentDate())
        #self.du_edit.setDisplayFormat("dd/MM/yyyy")
        self.du_edit.setCalendarPopup(True)
        self.du_edit.setStyleSheet("""
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

        self.date_visite_medicale_edit = QDateEdit(QDate.currentDate())
        #self.date_visite_medicale_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_visite_medicale_edit.setCalendarPopup(True)
        self.date_visite_medicale_edit.setStyleSheet("""
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

        self.date_accueil_securite_edit = QDateEdit(QDate.currentDate())
        #self.date_accueil_securite_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_accueil_securite_edit.setCalendarPopup(True)
        self.date_accueil_securite_edit.setStyleSheet("""
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

        self.msb_edit = QDateEdit(QDate.currentDate())
        #self.msb_edit.setDisplayFormat("dd/MM/yyyy")
        self.msb_edit.setCalendarPopup(True)
        self.msb_edit.setStyleSheet("""
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

        self.consignation_edit = QDateEdit(QDate.currentDate())
        #self.consignation_edit.setDisplayFormat("dd/MM/yyyy")
        self.consignation_edit.setCalendarPopup(True)
        self.consignation_edit.setStyleSheet("""
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

        self.ms_edit = QDateEdit(QDate.currentDate())
        #self.ms_edit.setDisplayFormat("dd/MM/yyyy")
        self.ms_edit.setCalendarPopup(True)
        self.ms_edit.setStyleSheet("""
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

        self.ve_omsi_edit = QDateEdit(QDate.currentDate())
        #self.ve_omsi_edit.setDisplayFormat("dd/MM/yyyy")
        self.ve_omsi_edit.setCalendarPopup(True)
        self.ve_omsi_edit.setStyleSheet("""
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

        layout.addWidget(QLabel("DU:"))
        layout.addWidget(self.du_edit)
        layout.addWidget(QLabel("Date visite médicale:"))
        layout.addWidget(self.date_visite_medicale_edit)
        layout.addWidget(QLabel("Date accueil sécurité:"))
        layout.addWidget(self.date_accueil_securite_edit)
        layout.addWidget(QLabel("MSB:"))
        layout.addWidget(self.msb_edit)
        layout.addWidget(QLabel("Consignation:"))
        layout.addWidget(self.consignation_edit)
        layout.addWidget(QLabel("MS:"))
        layout.addWidget(self.ms_edit)
        layout.addWidget(QLabel("VE_OMSI:"))
        layout.addWidget(self.ve_omsi_edit)


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