#view/step_one.py

import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout,QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QStackedWidget, QDateEdit, QMessageBox , QScrollArea
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter
from PyQt5.QtCore import Qt, QDate 


class StepOne(QScrollArea):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        content_widget = QWidget()
        layout = QVBoxLayout()
        content_widget.setLayout(layout)

        self.badge_edit = QLineEdit(self)


        self.photo_label = QLabel()
        self.photo_button = QPushButton("Import Photo")
        self.photo_data = None

        self.nom_edit = QLineEdit()
        self.prenom_edit = QLineEdit()
        self.cin_edit = QLineEdit()

        self.date_cin_edit = QDateEdit(QDate.currentDate())
        #self.date_cin_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_cin_edit.setCalendarPopup(True)

        self.lieu_cin_edit = QLineEdit()
        self.contact_edit = QLineEdit()

        self.date_naissance_edit = QDateEdit(QDate.currentDate())
        #self.date_naissance_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_naissance_edit.setCalendarPopup(True)

        self.lieu_naissance_edit = QLineEdit()
        self.adresse_edit = QLineEdit()
        self.equipe_combo = QComboBox()
        self.sous_categorie_combo = QComboBox()

        CIN_layout = QHBoxLayout()
        CIN_layout.addWidget(QLabel("CIN :"))
        CIN_layout.addWidget(self.cin_edit)
        CIN_layout.addWidget(QLabel("Date CIN :"))
        CIN_layout.addWidget(self.date_cin_edit)
        CIN_layout.addWidget(QLabel("Lieu CIN : "))
        CIN_layout.addWidget(self.lieu_cin_edit)

        Nom_prenom_layout = QHBoxLayout()
        Nom_prenom_layout.addWidget(QLabel("Nom :"))
        Nom_prenom_layout.addWidget(self.nom_edit)
        Nom_prenom_layout.addWidget(QLabel("Prenoms :"))
        Nom_prenom_layout.addWidget(self.prenom_edit)

        Date_lieu_naissance_layout = QHBoxLayout()
        Date_lieu_naissance_layout.addWidget(QLabel("Date de naissance :"))
        Date_lieu_naissance_layout.addWidget(self.date_naissance_edit)
        Date_lieu_naissance_layout.addWidget(QLabel("Lieu de naissance"))
        Date_lieu_naissance_layout.addWidget(self.lieu_naissance_edit)

        Equipe_souscategorie_layout = QHBoxLayout()
        Equipe_souscategorie_layout.setSpacing(0)
        Equipe_souscategorie_layout.addWidget(QLabel("Equipe :"))
        Equipe_souscategorie_layout.addWidget(self.equipe_combo)
        Equipe_souscategorie_layout.addWidget(QLabel("Categorie : "))
        Equipe_souscategorie_layout.addWidget(self.sous_categorie_combo)

        

        layout.addWidget(QLabel("Badge:"))
        layout.addWidget(self.badge_edit)

        layout.addLayout(Nom_prenom_layout)
        

        layout.addWidget(QLabel("Contact:"))
        layout.addWidget(self.contact_edit)

        layout.addLayout(CIN_layout)

        layout.addLayout(Date_lieu_naissance_layout)

        layout.addWidget(QLabel("Adresse:"))
        layout.addWidget(self.adresse_edit)

        layout.addLayout(Equipe_souscategorie_layout)

        layout.addWidget(QLabel("Photo:"))
        layout.addWidget(self.photo_label)
        layout.addWidget(self.photo_button)

        self.setWidget(content_widget)
        self.setWidgetResizable(True)

    def importer_photo(self):
        if self.photo_data is not None:
            # Si les données de la photo existent déjà, utilisez-les
            return self.photo_data

        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        photo_path, _ = QFileDialog.getOpenFileName(self, "Importer une photo", "", "Images (*.jpg *.png *.jpeg);;Tous les fichiers (*)", options=options)

        if photo_path:
            with open(photo_path, 'rb') as photo_file:
                photo_data = photo_file.read()
            image = QImage.fromData(photo_data)
            self.photo_label.setPixmap(QPixmap.fromImage(image).scaled(200, 200, Qt.KeepAspectRatio))
            self.photo_data = photo_data  # Stockez les données de la photo dans la variable de classe
            return photo_data