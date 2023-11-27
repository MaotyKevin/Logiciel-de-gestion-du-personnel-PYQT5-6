from model.admin_crud_model import Admin_crud_model

class AdminCrudController:
    def __init__(self, db_path):
        self.model = Admin_crud_model(db_path)

    def getTeamData(self):
        return self.model.getTeamData()
    
    def getUserData(self):
        return self.model.getUserData()
    
    def getAdminData(self):
        return self.model.getAdminData()
    
    def getCategorieData(self):
        return self.model.getCategorieData()
    
    def getSCData(self):
        return self.model.getSCData()

    def add_team(self, nom_equipe):
        self.model.addTeam(nom_equipe)

    def addCategorie(self , nom_categorie):
        self.model.addCategorie(nom_categorie)    

    def addSC(self , sousCategorie):
        self.model.addSC(sousCategorie)

    def delete_team(self, id_equipe):
        self.model.deleteTeam(id_equipe)

    def deleteCategorie( self , id_categorie):
        self.model.deleteCategorie(id_categorie)

    def deleteSC( self , id_sousCategorie):
        self.model.deleteSC(id_sousCategorie)

    def update_team(self, id_equipe, new_team_name):
        return self.model.updateTeam(id_equipe, new_team_name)

    def updateCategorie(self , id_categorie , nom_categorie):
        return self.model.updateCategorie(id_categorie , nom_categorie)    

    def updateSC(self , id_sousCategorie , sousCategorie):
        return self.model.updateSC(id_sousCategorie , sousCategorie)

    def add_User(self, username , password):
        self.model.addNewUser(username , password)

    def add_Admin(self , username , password):
        self.model.addNewAdmin(username , password)

    def delete_User(self, id_user):
        self.model.deleteUser(id_user)

    def delete_Admin(self , id_admin):
        self.model.deleteAdmin(id_admin)

    def update_Username(self, id_user, username):
        return self.model.updateUserName(id_user, username)
    
    def update_adminName(self , id_admin , adminName):
        return self.model.updateAdminName(id_admin , adminName)

    def update_Password(self , id_user , password):
        return self.model.updateUserPassword(id_user , password)
    
    def update_adminPassword(self , id_admin , adminPassword):
        return self.model.updateAdminPassword(id_admin , adminPassword)

    def verifyTeam(self , nom_equipe):
        return self.model.teamVerify(nom_equipe)
    
    def verifyCategorie(self , nom_categorie):
        return self.model.categorieerify(nom_categorie)

    def verifySC(self , sousCategorie):
        return self.model.SCVerify(sousCategorie)
    
    def verifyUsername(self , username):
        return self.model.UsernameVerify(username)
    
    def verifyAdminName(self , adminName):
        return self.model.AdminNameVerify(adminName)
    
    def verifyPassword(self , password):
        return self.model.PasswordVerify(password)
    
    def verifyAdminPassword(self , adminPassword):
        return self.model.AdminPasswordVerify(adminPassword)
    
    def verifyEmployeeTeam(self , id_equipe):
        return self.model.has_assigned_employees_Team(id_equipe)
    
    def verifyEmployeeCategorie(self , id_categorie):
        return self.model.has_assigned_employees_Categorie(id_categorie)
    
    def verifyEmployeeSC(self , id_sousCategorie):
        return self.model.has_assigned_employees_SC(id_sousCategorie)