# view/inscription_personnel_view.py
import sys , os
from PyQt5.QtWidgets import QApplication,QStackedWidget, QDialog, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog,QScrollArea , QDateEdit , QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QFont, QPainter
from PyQt5.QtCore import Qt , QDate, pyqtSignal


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from model.database import Databases
from view.step_one import StepOne
from view.step_two import StepTwo
from view.step_three import StepTree


class InscriptionPersonnelForm(QWidget):
    def __init__(self , db_path , controller):
        super().__init__()
       
        self.setGeometry(100, 100, 800, 600)
        self.current_step = 0
        self.initUI()
        
        self.db_model = Databases(db_path)
        self.controller = controller
       
        self.remplir_liste_equipe()
        self.remplir_liste_sous_categorie()
            

    def obtenir_id_equipe(self):
        selected_equipe = self.stepOne.equipe_combo.currentText()
        id_equipe = self.db_model.recuperer_id_equipe(selected_equipe)
        return id_equipe

    def obtenir_id_sous_categorie(self):
        # Récupérez le nom de la sous-catégorie sélectionnée dans la liste déroulante
        selected_sous_categorie = self.stepOne.sous_categorie_combo.currentText()

        """if selected_sous_categorie == "Aucun":
            return 'NULL'  # Si "Aucun" est sélectionné, retournez None """

        # Sinon, appelez la méthode du modèle pour obtenir l'ID de la sous-catégorie
        id_sous_categorie = self.db_model.recuperer_id_sous_categorie(selected_sous_categorie)

        return id_sous_categorie
    

    def remplir_liste_equipe(self):
        equipe_data = self.db_model.recuperer_donnees_equipe()
        self.stepOne.equipe_combo.addItems(equipe_data)

    def remplir_liste_sous_categorie(self):
        sous_categorie_data = self.db_model.recuperer_donnees_sous_categorie()
        self.stepOne.sous_categorie_combo.addItems(sous_categorie_data)

    def message_valide(self):
        
        QMessageBox.information(self , "Confirmation", "Les données ont été enregistrées avec succès.")

        # Réinitialisez les champs de saisie
        for widget in self.stepOne.findChildren(QLineEdit):
            widget.clear()
        
        for widget in self.stepTwo.findChildren(QLineEdit):
            widget.clear() 

        for widget in self.stepThree.findChildren(QLineEdit):
            widget.clear()      

        for widget in self.stepOne.findChildren(QDateEdit):
            widget.clear()

        for widget in self.stepTwo.findChildren(QDateEdit):
            widget.clear()

        for widget in self.stepThree.findChildren(QDateEdit):
            widget.clear()

        self.stepOne.photo_label.clear()
        self.stepOne.photo_data = None 
        self.stepOne.selectedSexe = None



    def initUI(self):

        self.step_widget = QStackedWidget(self)        
        self.stepOne = StepOne()
        self.stepTwo = StepTwo()
        self.stepThree = StepTree()
        
        self.step_widget.addWidget(self.stepOne)
        self.step_widget.addWidget(self.stepTwo)
        self.step_widget.addWidget(self.stepThree)

        self.prev_button = QPushButton("Precedent")
        self.prev_button.clicked.connect(self.show_previous_step)

        self.next_button = QPushButton("Suivant")
        self.next_button.clicked.connect(self.show_next_step)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.step_widget)
        main_layout.addLayout(button_layout)

        self.stepOne.photo_button.clicked.connect(self.stepOne.importer_photo)
        self.stepThree.enregistrer_button.clicked.connect(self.envoi)

        self.setLayout(main_layout) 

    def show_previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.step_widget.setCurrentIndex(self.current_step)
            self.updateButtonVisibility()

    def show_next_step(self):
        if self.current_step < self.step_widget.count() - 1:
            self.current_step += 1
            self.step_widget.setCurrentIndex(self.current_step)  
            self.updateButtonVisibility()

    def updateButtonVisibility(self):
        if self.current_step == 0:
            self.prev_button.setEnabled(False)
        else:
            self.prev_button.setEnabled(True)

        if self.current_step == self.step_widget.count() - 1:
            self.next_button.setEnabled(False)
        else:
            self.next_button.setEnabled(True)   
    
    def envoi(self):

        badge = self.stepOne.badge_edit.text()
        nom = self.stepOne.nom_edit.text()
        prenom = self.stepOne.prenom_edit.text()
        sexe = self.stepOne.capture_sexe()
        cin = self.stepOne.cin_edit.text()
        date_cin = self.stepOne.date_cin_edit.date().toString()
        lieu_cin = self.stepOne.lieu_cin_edit.text()
        contact = self.stepOne.contact_edit.text()
        date_naissance = self.stepOne.date_naissance_edit.date().toString()
        lieu_naissance = self.stepOne.lieu_naissance_edit.text()
        adresse = self.stepOne.adresse_edit.text()
        photo_data = self.stepOne.importer_photo()        

      
        du = self.stepTwo.du_edit.date().toString()
        date_visite_medicale = self.stepTwo.date_visite_medicale_edit.date().toString()
        date_accueil_securite = self.stepTwo.date_accueil_securite_edit.date().toString()
        msb = self.stepTwo.msb_edit.date().toString()
        consignation = self.stepTwo.consignation_edit.date().toString()
        ms = self.stepTwo.ms_edit.date().toString()
        ve_omsi = self.stepTwo.ve_omsi_edit.date().toString()

        
        fonction = self.stepThree.fonction_edit.text()
        deuxieme_fonction = self.stepThree.deuxieme_fonction_edit.text()
        categorie = self.stepThree.categorie_edit.text()
        date_debut = self.stepThree.date_debut_edit.date().toString()
        date_fin = self.stepThree.date_fin_edit.date().toString()
        cause_depart = self.stepThree.cause_depart_edit.text()

        date_equipement = self.stepThree.date_equipement_edit.date().toString()
        casque = self.stepThree.casque_edit.text()
        haut = self.stepThree.haut_edit.text()
        lunette = self.stepThree.lunette_edit.text()
        chaussure = self.stepThree.chaussure_edit.text()

        sous_categorie_id = self.obtenir_id_sous_categorie()
        equipe_id = self.obtenir_id_equipe()

        affectation_id = self.db_model.inserer_affectation(fonction , deuxieme_fonction , categorie , date_debut , date_fin , cause_depart , sous_categorie_id)

            

        equipement_id = self.db_model.inserer_equipement(date_equipement , casque , haut , lunette , chaussure)

        visite_id = self.db_model.inserer_visite(du , date_visite_medicale , date_accueil_securite , msb , consignation , ms , ve_omsi)

            

        self.controller.add_employee(badge , nom , prenom , sexe , cin , date_cin , lieu_cin , contact , date_naissance , lieu_naissance , adresse , photo_data , affectation_id , equipe_id , equipement_id , visite_id) 


        self.message_valide()
        
        
 






        



