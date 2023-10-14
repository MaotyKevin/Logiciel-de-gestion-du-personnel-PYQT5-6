#model/card_personnel_model.py

import sqlite3 , logging

class PersonnelCardModel:
    def __init__(self, db_path):
        self.db_path = str(db_path)

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            print("Database connection successful.")
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)



    def delete_card(self, Badge):
        # Configuration de la journalisation
        logging.basicConfig(filename='database_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

        try:
            self.connect()
            cursor = self.conn.cursor()
            
            #var = f"\"{Badge}\""
            #print(var)
            # Print the cleaned Badge value for debugging
            #print("Deleting card with ", cleaned_badge)
            #print(type(cleaned_badge))
            # Execute the DELETE query to remove the card from the database
      
            query = ("DELETE FROM Personnel WHERE Badge = ? ")
            cursor.execute(query , (Badge,))
            self.conn.commit()

        except sqlite3.Error as e:
            print("Error executing the query:", e)
            logging.error("Erreur lors de l'exécution de la requête SQL : %s", e)
       

    def get_employee_details(self, Badge ):
        try:
            self.connect()  # Connect to the database
            cursor = self.conn.cursor()
            query = """
            SELECT 
                P.Badge, P.Nom, P.Sexe 
            FROM Personnel P WHERE Badge = ? """
            print(f"Badge : {Badge}")
            
            cursor.execute(query, (Badge,))
            employeeDetails = cursor.fetchone()  # Use fetchone() to retrieve a single row
            print(f"Employee details = {employeeDetails}")
            return employeeDetails

        except sqlite3.Error as e:
            print("Error executing the query:", e)
     
       
 

    def get_personnel_data(self):
        try:
            self.connect()  # Connect to the database
            cursor = self.conn.cursor()
            query = """SELECT 
            P.Badge, P.Nom, 
            COALESCE(A.Categorie, 'Aucun') AS Categorie,
            COALESCE(A.Fonction, 'Aucun') AS Fonction,
            COALESCE(S.sousCategorie, 'Aucun') AS sousCategorie 

            FROM Personnel P 
            LEFT JOIN Affectation A ON P.id_affectation = A.id_affectation 
            LEFT JOIN SousCategorie S ON A.id_sousCategorie = S.id_sousCategorie"""
            
            cursor.execute(query)
            self.conn.commit()  # Commit the transaction if needed
            

            
            personnel_data = cursor.fetchall()

            
            
            return personnel_data
            
            
        except sqlite3.Error as e:
            print("Error executing the query:", e)
         # Close the database connection

# Test the model by creating an instance and calling the method
if __name__ == "__main__":
    db_path = 'data/my_database.sqlite'
    Databasess = PersonnelCardModel(db_path)
    Databasess.get_employee_details("543454")
