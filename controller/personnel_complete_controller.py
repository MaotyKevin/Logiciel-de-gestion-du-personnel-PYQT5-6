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

if __name__ == "__main__":
    db_path = 'data\my_database.sqlite'
    controller = Complete_controller(db_path)
    perso , equipe , categ , sc , affect , equipement , visite = controller.get_complete_info(5443)

    print(perso)