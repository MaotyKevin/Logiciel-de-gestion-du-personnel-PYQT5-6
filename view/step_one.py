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
        #sexe_layout.addWidget(QLabel("Sexe:"))
        for sexe_value in sexe_values:
            radio = QRadioButton(sexe_value)
            radio.clicked.connect(self.capture_sexe)
            sexe_layout.addWidget(radio)
            self.sexe_radios.append(radio)


        self.badge_edit = QLineEdit(self)
        self.badge_edit.setPlaceholderText("Badge")
        self.badge_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #734001; /* Blue border */
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
                border: 1px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.prenom_edit = QLineEdit()
        self.prenom_edit.setPlaceholderText("Prenoms")
        self.prenom_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)
        

        self.cin_edit = QLineEdit()
        self.cin_edit.setPlaceholderText("Numero de CIN")
        self.cin_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.date_cin_edit = QDateEdit(QDate.currentDate())
        self.date_cin_edit.setStyleSheet("""
            QDateEdit {
                border: 1px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        
            QDateEdit::down-arrow {background-color: #734001;}
        """)
        #self.date_cin_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_cin_edit.setCalendarPopup(True)
      

        self.lieu_cin_edit = QLineEdit()
        self.lieu_cin_edit.setPlaceholderText("Lieu CIN")
        self.lieu_cin_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.contact_edit = QLineEdit()
        self.contact_edit.setPlaceholderText("Contact")
        self.contact_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)        

        self.date_naissance_edit = QDateEdit(QDate.currentDate())
        self.date_naissance_edit.setStyleSheet("""
            QDateEdit {
                border: 1px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        
            QDateEdit::down-arrow {background-color: #734001;}
        """)
        #self.date_naissance_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_naissance_edit.setCalendarPopup(True)
        

        self.lieu_naissance_edit = QLineEdit()
        self.lieu_naissance_edit.setPlaceholderText("Lieu de naissance")
        self.lieu_naissance_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #734001; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                padding: 8px; /* Add padding */
                background-color: #FFFFFF; /* White background */
            }
        """)

        self.adresse_edit = QLineEdit()
        self.adresse_edit.setPlaceholderText("Adresse")
        self.adresse_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #734001; /* Blue border */
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

#__________________________LES FRAMES___________________________________________________

        infoPerso_container = QFrame()
        
        infoPerso_container.setObjectName("NameContainer")
        infoPerso_container.setStyleSheet("""
            QFrame#NameContainer {
                border: 1px solid gray; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                background-color: white; /* Semi-transparent white background */
            }
        """)

        Coordonnees_container = QFrame()
        
        Coordonnees_container.setObjectName("Coordonnees_container")
        Coordonnees_container.setStyleSheet("""
            QFrame#Coordonnees_container {
                border: 1px solid gray; /* Blue border */
                border-radius: 10px; /* Rounded corners */
                background-color: white; /* Semi-transparent white background */
            }
        """)



#___________________________________ASSEMBLAGES___________________________________________
        

        Nom_prenom_layout = QHBoxLayout()
        #Nom_prenom_layout.addWidget(QLabel("Nom :"))
        Nom_prenom_layout.addWidget(self.nom_edit)
        #Nom_prenom_layout.addWidget(QLabel("Prenoms :"))
        Nom_prenom_layout.addWidget(self.prenom_edit)

        Date_lieu_naissance_layout = QHBoxLayout()
        Date_lieu_naissance_layout.addWidget(self.lieu_naissance_edit)
        Date_lieu_naissance_layout.addWidget(self.date_naissance_edit)

        Equipe_souscategorie_layout = QHBoxLayout()
        Equipe_souscategorie_layout.addLayout(self.equipeLayout)
        #Equipe_souscategorie_layout.addWidget(self.equipe_combo)
        Equipe_souscategorie_layout.addLayout(self.SCategLayout)
        #Equipe_souscategorie_layout.addWidget(self.sous_categorie_combo)

        CIN_layout = QHBoxLayout()
        CIN_layout.addWidget(self.cin_edit)
        CIN_layout.addWidget(self.lieu_cin_edit)
        CIN_layout.addWidget(self.date_cin_edit)

#_____________________________________CASES________________________________________
        
        Info_perso_layout = QVBoxLayout(infoPerso_container)
        Info_perso_layout.addWidget(self.badge_edit)
        Info_perso_layout.addLayout(Nom_prenom_layout)
        Info_perso_layout.addLayout(sexe_layout)
        Info_perso_layout.addLayout(Date_lieu_naissance_layout)

        info_perso_label = QLabel("Informations personnelles")
        info_perso_label.setStyleSheet("font-weight: bolder; color:black;")

        info_perso = QVBoxLayout()
        info_perso.addWidget(info_perso_label)
        info_perso.addWidget(infoPerso_container)

        Coordonnees_layout = QVBoxLayout(Coordonnees_container)
        Coordonnees_layout.addWidget(self.contact_edit)
        Coordonnees_layout.addLayout(CIN_layout)
        Coordonnees_layout.addWidget(self.adresse_edit)

        coordonnees_label = QLabel("Coordonnees")
        coordonnees_label.setStyleSheet("font-weight: bolder; color:black;")

        coordonnees = QVBoxLayout()
        coordonnees.addWidget(coordonnees_label)
        coordonnees.addWidget(Coordonnees_container)
        

#________________________________MISE EN PAGE_______________________________________________

  
        layout.addLayout(info_perso)
        layout.addLayout(coordonnees)
        layout.addLayout(Equipe_souscategorie_layout)

        layout.addWidget(QLabel("Photo:"))
        layout.addWidget(self.photo_label)
        layout.addWidget(self.photo_button)
        layout.setSpacing(15)

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