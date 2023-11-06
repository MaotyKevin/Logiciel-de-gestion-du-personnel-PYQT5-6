import sys , os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from model.admin_model import DatabaseHandler

class ChatController():
    def __init__(self, db_path):
        self.model = DatabaseHandler(db_path)

    def sampleUserName(self):
        return self.model.sampleUserName()
    
if __name__ == "__main__":
    db_path = 'data\my_database.sqlite'
    controller = ChatController(db_path)
    names = controller.sampleUserName()
    for column in names :
        print(f'\n{column}')
