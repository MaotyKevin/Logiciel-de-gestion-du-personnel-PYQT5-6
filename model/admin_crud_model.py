import sqlite3
import io

class Admin_crud_model:
    def __init__(self , db_path):
        self.db_path = str(db_path)
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()  

    def getAdminData(self):
        query = """
            SELECT id , Username , Password FROM Admin
        """

        self.cursor.execute(query)
        self.connection.commit()

        AdminData = self.cursor.fetchall()
        return AdminData
    
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
            INSERT INTO User (Username , Password , id_role) VALUES (? , ? , ?)
        """
        userRole = int(2)
        self.cursor.execute(add_query , (username , password,userRole))
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
            print(f"Error updating User: {e}")
            return False
        
#________________________________________________

    def addNewAdmin(self , username , password):
        add_query = """
            INSERT INTO Admin (Username , Password , id_role) VALUES (? , ? , ?)
        """
        adminRole = int(1)
        self.cursor.execute(add_query , (username , password,adminRole))
        self.connection.commit()

    def deleteAdmin(self , id_admin):
        delete_query = """
            DELETE FROM Admin WHERE id = ?
        """
        self.cursor.execute(delete_query , (id_admin,))
        self.connection.commit()

    def updateAdminName(self , id_admin , adminName):
        try:
            update_query = "UPDATE Admin SET Username = ? WHERE id = ?"
            self.cursor.execute(update_query, (adminName, id_admin))
            self.connection.commit()
            return True  # Return True to indicate success
        except sqlite3.Error as e:
            print(f"Error updating Admin username: {e}")
            return False
        
    def updateAdminPassword(self , id_admin , adminPassword):
        try:
            update_query = "UPDATE Admin SET Password = ? WHERE id = ?"
            self.cursor.execute(update_query, (adminPassword, id_admin))
            self.connection.commit()
            return True  # Return True to indicate success
        except sqlite3.Error as e:
            print(f"Error updating Admin password: {e}")
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
        
#___________________________________________________

    def teamVerify(self , nom_equipe):
        query = "SELECT COUNT(*) FROM Equipe WHERE nom_equipe = ?"
        result = self.cursor.execute(query, (nom_equipe,)).fetchone()
        self.connection.commit()
        return result[0] > 0
    
    def SCVerify(self , sousCategorie):
        query = "SELECT COUNT(*) FROM SousCategorie WHERE sousCategorie = ?"
        result = self.cursor.execute(query, (sousCategorie,)).fetchone()
        self.connection.commit()
        return result[0] > 0

    def UsernameVerify(self , username):
        query = "SELECT COUNT(*) FROM User WHERE Username = ?"
        result = self.cursor.execute(query, (username,)).fetchone()
        self.connection.commit()
        return result[0] > 0
    
    def PasswordVerify(self , password):
        query = "SELECT COUNT(*) FROM User WHERE Password = ?"
        result = self.cursor.execute(query, (password,)).fetchone()
        self.connection.commit()
        return result[0] > 0
    
    def AdminNameVerify(self , username):
        query = "SELECT COUNT(*) FROM Admin WHERE Username = ?"
        result = self.cursor.execute(query, (username,)).fetchone()
        self.connection.commit()
        return result[0] > 0
    
    def AdminPasswordVerify(self , password):
        query = "SELECT COUNT(*) FROM Admin WHERE Password = ?"
        result = self.cursor.execute(query, (password,)).fetchone()
        self.connection.commit()
        return result[0] > 0

# Example usage:
if __name__ == "__main__":
    db_path = 'data\my_database.sqlite'
    Admin_crud_models = Admin_crud_model(db_path)

    