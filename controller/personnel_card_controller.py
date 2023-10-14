#personnel_card_controller.py

import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from model.card_personnel_model import PersonnelCardModel

class PersonnelController:
    def __init__(self, db_path):
        self.model = PersonnelCardModel(db_path)

    def get_personnel_data(self):
        return self.model.get_personnel_data()
    
    def get_employee_details(self , Badge):
        print("contro get employee details called")
        return self.model.get_employee_details(Badge)
    
    def delete_data(self , Badge):
        print("Controller delete called")
        return self.model.delete_card(Badge)

if __name__ == "__main__":
    contro = PersonnelController('data/my_database.sqlite')
    contro.get_employee_details("543454")