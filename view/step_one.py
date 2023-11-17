#view/step_one.py

import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QRadioButton, QVBoxLayout,QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QStackedWidget, QDateEdit, QMessageBox , QScrollArea , QFrame
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter
from PyQt5.QtCore import Qt, QDate 


class StepOne(QScrollArea):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.selectedSexe = None

    def initUI(self):
        content_widget = QWidget()
        layout = QVBoxLayout()
        content_widget.setLayout(layout)

        sexe_values = ["Homme", "Femme"]
        self.sexe_radios = []
        sexe_layout = QHBoxLayout()
        sexe_layout.addWidget(QLabel("Sexe:"))
        for sexe_value in sexe_values:
            radio = QRadioButton(sexe_value)
            radio.clicked.connect(self.capture_sexe)
            sexe_layout.addWidget(radio)
            self.sexe_radios.append(radio)


        self.badge_edit = QLineEdit(self)
        self.badge_edit.setPlaceholderText("Badge")
        self.badge_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)


        self.photo_label = QLabel()
        self.photo_button = QPushButton("Importer une photo")
        self.photo_data = None

        self.nom_edit = QLineEdit()
        self.nom_edit.setPlaceholderText("Nom")
        self.nom_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.prenom_edit = QLineEdit()
        self.prenom_edit.setPlaceholderText("Prenoms")
        self.prenom_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)
        

        self.cin_edit = QLineEdit()
        self.cin_edit.setPlaceholderText("Numero de CIN")
        self.cin_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.date_cin_edit = QDateEdit(QDate.currentDate())
        #self.date_cin_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_cin_edit.setCalendarPopup(True)
      

        self.lieu_cin_edit = QLineEdit()
        self.lieu_cin_edit.setPlaceholderText("Lieu CIN")
        self.lieu_cin_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.contact_edit = QLineEdit()
        self.contact_edit.setPlaceholderText("Contact")
        self.contact_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)        

        self.date_naissance_edit = QDateEdit(QDate.currentDate())
        #self.date_naissance_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_naissance_edit.setCalendarPopup(True)
        

        self.lieu_naissance_edit = QLineEdit()
        self.lieu_naissance_edit.setPlaceholderText("Lieu de naissance")
        self.lieu_naissance_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.adresse_edit = QLineEdit()
        self.adresse_edit.setPlaceholderText("Adresse")
        self.adresse_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.equipeLayout = QVBoxLayout()
        self.equipe_combo = QComboBox()
        self.equipeLayout.addWidget(QLabel("Equipe"))
        self.equipeLayout.addWidget(self.equipe_combo)

        self.SCategLayout = QVBoxLayout()
        self.sous_categorie_combo = QComboBox()
        self.SCategLayout.addWidget(QLabel("Sous-categorie"))
        self.SCategLayout.addWidget(self.sous_categorie_combo)

        CIN_layout = QHBoxLayout()
        #CIN_layout.addWidget(QLabel("CIN :"))
        CIN_layout.addWidget(self.cin_edit)
        #CIN_layout.addWidget(QLabel("Date CIN :"))
        CIN_layout.addWidget(self.date_cin_edit)
        #CIN_layout.addWidget(QLabel("Lieu CIN : "))
        CIN_layout.addWidget(self.lieu_cin_edit)

        name_container = QFrame()
        
        name_container.setObjectName("NameContainer")
        name_container.setStyleSheet("""
            QFrame#NameContainer {
                border: 1px solid gray; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                background-color: white; /* Semi-transparent white background */
            }
        """)
        Nom_prenom_layout = QHBoxLayout(name_container)
        #Nom_prenom_layout.addWidget(QLabel("Nom :"))
        Nom_prenom_layout.addWidget(self.nom_edit)
        #Nom_prenom_layout.addWidget(QLabel("Prenoms :"))
        Nom_prenom_layout.addWidget(self.prenom_edit)

        Date_lieu_naissance_layout = QHBoxLayout()
        #Date_lieu_naissance_layout.addWidget(QLabel("Date de naissance :"))
        Date_lieu_naissance_layout.addWidget(self.date_naissance_edit)
        #Date_lieu_naissance_layout.addWidget(QLabel("Lieu de naissance"))
        Date_lieu_naissance_layout.addWidget(self.lieu_naissance_edit)

        Equipe_souscategorie_layout = QHBoxLayout()
        Equipe_souscategorie_layout.addLayout(self.equipeLayout)
        #Equipe_souscategorie_layout.addWidget(self.equipe_combo)
        Equipe_souscategorie_layout.addLayout(self.SCategLayout)
        #Equipe_souscategorie_layout.addWidget(self.sous_categorie_combo)
        
        

        #layout.addWidget(QLabel("Badge:"))
        layout.addWidget(self.badge_edit)

        layout.addWidget(name_container)

        layout.addLayout(sexe_layout)
        

        #layout.addWidget(QLabel("Contact:"))
        layout.addWidget(self.contact_edit)

        layout.addLayout(CIN_layout)

        layout.addLayout(Date_lieu_naissance_layout)

        #layout.addWidget(QLabel("Adresse:"))
        layout.addWidget(self.adresse_edit)

        layout.addLayout(Equipe_souscategorie_layout)

        layout.addWidget(QLabel("Photo:"))
        layout.addWidget(self.photo_label)
        layout.addWidget(self.photo_button)
        layout.setSpacing(10)

        self.setWidget(content_widget)
        self.setWidgetResizable(True)

    
        

    def capture_sexe(self):
        # Check which radio button is checked and capture the selected "sexe" value
        for radio in self.sexe_radios:
            if radio.isChecked():
                self.selectedSexe = radio.text()
                return self.selectedSexe

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
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    stepOne = StepOne()
    stepOne.show()
    sys.exit(app.exec_())