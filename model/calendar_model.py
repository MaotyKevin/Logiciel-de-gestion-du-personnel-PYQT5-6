import sqlite3

class Employee_VEOMSI_Model:
    def __init__(self, database_name):
        self.database_name = database_name

    def get_all_VE_OMSI_visits(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Select all visit dates from the Visite table
        query = """
            SELECT VE_OMSI
            FROM Visite
        """
        cursor.execute(query)

        visit_dates = cursor.fetchall()

        # Extract the dates from the result
        visit_dates = [date[0] for date in visit_dates]

        return visit_dates

    def get_employees_for_date(self, selected_date):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Joining Employee and Visit tables using the foreign key
        query = f"""
            SELECT P.Badge, P.Nom , P.Prenom , P.CIN , v.DU , A.Fonction , C.nom_categorie 
            FROM Personnel P
            LEFT JOIN Affectation A ON P.id_affectation = A.id_affectation
            LEFT JOIN Categorie C ON A.id_categorie = C.id_categorie
            LEFT JOIN Visite v ON P.id_visite = v.id_visite
            WHERE v.VE_OMSI = '{selected_date}'
        """
        cursor.execute(query)

        employees = cursor.fetchall()
        

        return employees
    
if __name__ == '__main__':
    model = Employee_VEOMSI_Model("data\my_database.sqlite")
    all_visits = model.get_all_VE_OMSI_visits()
    print(all_visits)