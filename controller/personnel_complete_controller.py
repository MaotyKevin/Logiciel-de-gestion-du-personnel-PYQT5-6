import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from model.personnel_complete_model import Complete_model

class Complete_controller:
    def __init__(self , db_path):
        self.db_path = db_path
        self.model = Complete_model(self.db_path)

    def get_complete_info(self , badge):
        personnelInfo = self.model.getPersonnelTable(badge)
        equipeInfo = self.model.get_EquipeInfo_table(badge)
        equipementInfo = self.model.getEquipementsTable(badge)
        visiteInfo = self.model.getVisiteTable(badge)
        affectationInfo = self.model.getAffectationTable(badge)
        categorieInfo = self.model.getCategoryTable(badge)
        SCInfo = self.model.getSCTable(badge)

        return personnelInfo , equipeInfo , categorieInfo , SCInfo , affectationInfo , equipementInfo , visiteInfo
    
    def update_personnelTable(self , badge , field , value):
        return self.model.update_personnel_model(badge , field , value)
    
    def update_EquipementTable(self , badge , field , value):
        return self.model.update_equipement_model(badge , field , value)

    def update_visiteTable(self , badge , field , value):
        return self.model.update_visite_model(badge , field , value)
    
    def update_affectationTable(self , badge , field , value):
        return self.model.update_affectation_model(badge , field , value)
    
#_________________________________________________

    def recuperer_id_categorie(self , categorie):
        return self.model.recuperer_id_categorie(categorie)
    
    def recuperer_id_equipe(self , equipe):
        return self.model.recuperer_id_equipe(equipe)
    
    def recuperer_id_SC(self , SC):
        return self.model.recuperer_id_sous_categorie(SC)
    
    def recuperer_donnees_categorie(self):
        return self.model.recuperer_donnees_categorie()
    
    def recuperer_donnees_equipe(self):
        return self.model.recuperer_donnees_equipe()
    
    def recuperer_donnees_SC(self):
        return self.model.recuperer_donnees_sous_categorie()


if __name__ == "__main__":
    db_path = 'data\my_database.sqlite'
    controller = Complete_controller(db_path)
    sc = controller.recuperer_donnees_SC()
    print(sc)