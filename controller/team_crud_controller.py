from model.admin_crud_model import Admin_crud_model

class AdminCrudController:
    def __init__(self, db_path):
        self.model = Admin_crud_model(db_path)

    def getTeamData(self):
        return self.model.getTeamData()

    def add_team(self, nom_equipe):
        self.model.addTeam(nom_equipe)

    def delete_team(self, id_equipe):
        self.model.deleteTeam(id_equipe)

    def update_team(self, id_equipe, new_team_name):
        return self.model.updateTeam(id_equipe, new_team_name)