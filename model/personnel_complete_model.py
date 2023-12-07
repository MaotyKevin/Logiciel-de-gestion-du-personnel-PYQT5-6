import sqlite3

class Complete_model:
    def __init__(self, database_name):
        self.database_name = database_name

    def update_personnel_model(self , badge , field , value):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = f"UPDATE Personnel SET {field} = ? WHERE Badge = ?"

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
    badge = 5443
    field = "Nom"
    value = "POKAHONTAS"
    Databasess.update_personnel_model(badge , field , value)