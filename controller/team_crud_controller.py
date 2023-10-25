from model.admin_crud_model import Admin_crud_model

class AdminCrudController:
    def __init__(self, db_path):
        self.model = Admin_crud_model(db_path)

    def getTeamData(self):
        return self.model.getTeamData()
    
    def getUserData(self):
        return self.model.getUserData()

    def add_team(self, nom_equipe):
        self.model.addTeam(nom_equipe)

    def delete_team(self, id_equipe):
        self.model.deleteTeam(id_equipe)

    def update_team(self, id_equipe, new_team_name):
        return self.model.updateTeam(id_equipe, new_team_name)
    
    def add_User(self, username , password):
        self.model.addNewUser(username , password)

    def delete_User(self, id_user):
        self.model.deleteUser(id_user)

    def update_Username(self, id_user, username):
        return self.model.updateUserName(id_user, username)
    
    def update_Password(self , id_user , password):
        return self.model.updateUserPassword(id_user , password)