import sqlite3
import io

class Admin_crud_model:
    def __init__(self , db_path):
        self.db_path = str(db_path)
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()  

    def getUserData(self):
        query = """
            SELECT id , Username , Password FROM User
        """

        self.cursor.execute(query)
        self.connection.commit()

        UserData = self.cursor.fetchall()
        return UserData   

    def getTeamData(self):
        query = """
            SELECT id_equipe , nom_equipe FROM Equipe
        """

        self.cursor.execute(query)
        self.connection.commit()

        teamData = self.cursor.fetchall()
        return teamData

    def addTeam(self , nom_equipe):
        insert_query = """
            INSERT INTO Equipe (nom_equipe) VALUES (?)
        """
        self.cursor.execute(insert_query , (nom_equipe,))
        self.connection.commit()

    def deleteTeam(self , id_equipe):
        delete_query = """
            DELETE FROM Equipe WHERE id_equipe = ?
        """
        self.cursor.execute(delete_query , (id_equipe,))
        self.connection.commit()

    def updateTeam(self , id_equipe , newTeamName):
        try:
            update_query = "UPDATE Equipe SET nom_equipe = ? WHERE id_equipe = ?"
            self.cursor.execute(update_query, (newTeamName, id_equipe))
            self.connection.commit()
            return True  # Return True to indicate success
        except sqlite3.Error as e:
            print(f"Error updating team: {e}")
            return False
        
    def addNewUser(self , username , password):
        add_query = """
            INSERT INTO User (Username , Password) VALUES (? , ?)
        """
        self.cursor.execute(add_query , (username , password,))
        self.connection.commit()

    def deleteUser(self , id_user):
        delete_query = """
            DELETE FROM User WHERE id = ?
        """
        self.cursor.execute(delete_query , (id_user,))
        self.connection.commit()

    def updateUserName(self , id_User , userName):
        try:
            update_query = "UPDATE User SET Username = ? WHERE id = ?"
            self.cursor.execute(update_query, (userName, id_User))
            self.connection.commit()
            return True  # Return True to indicate success
        except sqlite3.Error as e:
            print(f"Error updating team: {e}")
            return False
        
    def updateUserPassword(self , id_User , userPassword):
        try:
            update_query = "UPDATE User SET Password = ? WHERE id = ?"
            self.cursor.execute(update_query, (userPassword, id_User))
            self.connection.commit()
            return True  # Return True to indicate success
        except sqlite3.Error as e:
            print(f"Error updating team: {e}")
            return False

#____________________________________________________________________________________________________


    def getSCData(self):
        query = """
            SELECT id_sousCategorie , sousCategorie FROM SousCategorie
        """

        self.cursor.execute(query)
        self.connection.commit()

        SCData = self.cursor.fetchall()
        return SCData

    def addSC(self , sousCategorie):
        insert_query = """
            INSERT INTO SousCategorie (sousCategorie) VALUES (?)
        """
        self.cursor.execute(insert_query , (sousCategorie,))
        self.connection.commit()

    def deleteSC(self , id_sousCategorie):
        delete_query = """
            DELETE FROM SousCategorie WHERE id_sousCategorie = ?
        """
        self.cursor.execute(delete_query , (id_sousCategorie,))
        self.connection.commit()

    def updateSC(self , id_sousCategorie , sousCategorie):
        try:
            update_query = "UPDATE SousCategorie SET sousCategorie = ? WHERE id_sousCategorie = ?"
            self.cursor.execute(update_query, (sousCategorie, id_sousCategorie))
            self.connection.commit()
            return True  # Return True to indicate success
        except sqlite3.Error as e:
            print(f"Error updating team: {e}")
            return False
        
# Example usage:
if __name__ == "__main__":
    db_path = 'data\my_database.sqlite'
    Admin_crud_models = Admin_crud_model(db_path)
    """team = "Z"
    Admin_crud_models.addTeam(team)"""
    """
    new_name_team = "Nettoyage"
    Admin_crud_models.updateTeam(4 , new_name_team)
    """
    #teamlist = Admin_crud_models.getTeamData()
    #print(teamlist)

    Admin_crud_models.addSC("Nouveau test")
    

    #Admin_crud_models.deleteTeam(4)
    