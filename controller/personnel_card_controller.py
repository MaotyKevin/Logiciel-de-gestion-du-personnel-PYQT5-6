#personnel_card_controller.py

from model.card_personnel_model import PersonnelCardModel

class PersonnelController:
    def __init__(self, db_path):
        self.model = PersonnelCardModel(db_path)

    def get_personnel_data(self):
        return self.model.get_personnel_data()
    
    def delete_data(self , Badge):
        print("Controller delete called")
        return self.model.delete_card(Badge)
