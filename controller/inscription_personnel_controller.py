# controller/inscription_personnel_controller.py
from model.database import Databases
from view.inscription_personnel_view import InscriptionPersonnelForm


class InscriptionPersonnelController:
    def __init__(self ):
        self.view = None 
        self.model = Databases("data/my_database.sqlite")
        

    def add_employee(self , badge, nom, prenom, cin, date_cin, lieu_cin, contact, date_naissance, lieu_naissance, adresse, photo_data, affectation_id, id_equipe, id_equipement, id_visite):
        self.model.inserer_personnel( badge, nom, prenom, cin, date_cin, lieu_cin, contact, date_naissance, lieu_naissance, adresse, photo_data, affectation_id, id_equipe, id_equipement, id_visite) 
        print(f"Insertion personnel , ex : badge = {badge}")
        
        
