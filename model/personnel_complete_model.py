import sqlite3

class Complete_model:
    def __init__(self, database_name):
        self.database_name = database_name

    def recuperer_id_categorie(self,categorie):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()            
            cursor.execute("SELECT id_categorie FROM Categorie WHERE nom_categorie = ?" , (categorie,))
            row = cursor.fetchone()
            if row :
                return row[0]
            else :
                return None
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération de l'ID de la categorie : {str(e)}")
            return None

    def recuperer_id_equipe(self,equipe):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()            
            cursor.execute("SELECT id_equipe FROM Equipe WHERE nom_equipe = ?" , (equipe,))
            row = cursor.fetchone()
            if row :
                return row[0]
            else :
                return None
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération de l'ID de l'equipe : {str(e)}")
            return None
        
    def recuperer_id_sous_categorie(self, sous_categorie):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()         
            cursor.execute("SELECT id_sousCategorie FROM SousCategorie WHERE sousCategorie = ?", (sous_categorie,))
            row = cursor.fetchone()
            if row:
                return row[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération de l'ID de sous-catégorie : {str(e)}")
            return None
        
    def recuperer_donnees_categorie(self):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()            
            cursor.execute("SELECT nom_categorie FROM Categorie")
            categorie_data = [row[0] for row in cursor.fetchall()]
            return categorie_data
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données de categorie : {str(e)}")
            return []    


    def recuperer_donnees_equipe(self):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()            
            cursor.execute("SELECT nom_equipe FROM Equipe")
            equipe_data = [row[0] for row in cursor.fetchall()]
            return equipe_data
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données d'équipe : {str(e)}")
            return []

    def recuperer_donnees_sous_categorie(self):
        try:

            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
          
            cursor.execute("SELECT sousCategorie FROM SousCategorie")
            sous_categorie_data = ["Aucun"]  # Option "Aucun"
            sous_categorie_data += [row[0] for row in cursor.fetchall()]
            return sous_categorie_data
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données de sous-catégorie : {str(e)}")
            return []

#__________________________________________________

    def update_personnel_model(self , badge , field , value):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = f"UPDATE Personnel SET {field} = ? WHERE Badge = ?"

        cursor.execute(query , (value , badge) )
        conn.commit()
        return True
    def update_equipement_model(self , badge , field , value):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = f"UPDATE Equipement SET {field} = ? WHERE id_equipement = (SELECT id_equipement FROM Personnel WHERE Badge = ?)"

        cursor.execute(query , (value , badge) )
        conn.commit()
        return True 
    
    def update_visite_model(self , badge , field , value):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = f"UPDATE Visite SET {field} = ? WHERE id_visite = (SELECT id_visite FROM Personnel WHERE Badge = ?)"

        cursor.execute(query , (value , badge) )
        conn.commit()
        return True 
    
    def update_affectation_model(self , badge , field , value):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = f"UPDATE Affectation SET {field} = ? WHERE id_affectation = (SELECT id_affectation FROM Personnel WHERE Badge = ?)"

        cursor.execute(query , (value , badge) )
        conn.commit()
        return True 

    def get_EquipeInfo_table(self , Badge):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT E.nom_equipe FROM Personnel P 
            LEFT JOIN Equipe E ON P.id_equipe = E.id_equipe
            WHERE P.Badge = ? 
        """

        cursor.execute(query, (Badge,))
        employeeDetails = cursor.fetchone()  # Use fetchone() to retrieve a single row
        return employeeDetails
    
    def getPersonnelTable(self , Badge):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT Nom , Prenom , Sexe , CIN , Date_CIN , Lieu_CIN , Contact , Date_Naissance , Lieu_Naissance , Adresse FROM Personnel
            WHERE Badge = ? 
        """

        cursor.execute(query, (Badge,))
        employeeDetails = cursor.fetchone()  # Use fetchone() to retrieve a single row
        return employeeDetails
    
    def getEquipementsTable(self , Badge):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT E.DateEquipement , E.Casque , E.Haut , E.Lunette , E.Chaussure FROM Personnel P 
            LEFT JOIN Equipement E ON P.id_equipement = E.id_equipement
            WHERE P.Badge = ? 
        """

        cursor.execute(query, (Badge,))
        employeeDetails = cursor.fetchone()  # Use fetchone() to retrieve a single row
        return employeeDetails
    
    def getVisiteTable(self , Badge):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT V.DU , V.DateVisiteMedicale , V.DateAccueilSecurite , V.MSB , V.Consignation , V.MS , V.VE_OMSI FROM Personnel P 
            LEFT JOIN Visite V ON P.id_visite = V.id_visite
            WHERE P.Badge = ? 
        """

        cursor.execute(query, (Badge,))
        employeeDetails = cursor.fetchone()  # Use fetchone() to retrieve a single row
        return employeeDetails
    
    def getAffectationTable(self , Badge):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT A.Fonction , A.DeuxiemeFonction , A.DateDebut , A.DateFin , A.CauseDepart FROM Personnel P 
            LEFT JOIN Affectation A ON P.id_affectation = A.id_affectation
            WHERE P.Badge = ? 
        """

        cursor.execute(query, (Badge,))
        employeeDetails = cursor.fetchone()  # Use fetchone() to retrieve a single row
        return employeeDetails
    
    def getCategoryTable(self , Badge):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT C.nom_categorie FROM Personnel P 
            LEFT JOIN Affectation A ON P.id_affectation = A.id_affectation
            LEFT JOIN Categorie C ON A.id_categorie = C.id_categorie
            WHERE P.Badge = ? 
        """

        cursor.execute(query, (Badge,))
        employeeDetails = cursor.fetchone()  # Use fetchone() to retrieve a single row
        return employeeDetails
    
    def getSCTable(self , Badge):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT SC.sousCategorie FROM Personnel P 
            LEFT JOIN Affectation A ON P.id_affectation = A.id_affectation
            LEFT JOIN SousCategorie SC ON A.id_sousCategorie = SC.id_sousCategorie
            WHERE P.Badge = ? 
        """

        cursor.execute(query, (Badge,))
        employeeDetails = cursor.fetchone()  # Use fetchone() to retrieve a single row
        return employeeDetails
    
if __name__ == "__main__":
    db_path = 'data\my_database.sqlite'
    Databasess = Complete_model(db_path)
    categ = "USINE"
    data = Databasess.recuperer_id_categorie(categ)
    print(data)