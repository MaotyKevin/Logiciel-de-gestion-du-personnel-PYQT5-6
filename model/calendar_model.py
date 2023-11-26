import sqlite3

class Employee_VEOMSI_Model:
    def __init__(self, database_name):
        self.database_name = database_name

    def get_employees_for_date(self, selected_date):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Joining Employee and Visit tables using the foreign key
        query = f"""
            SELECT P.Badge, P.Nom , P.Prenom , P.CIN , A.Fonction , A.Categorie
            FROM Personnel P
            LEFT JOIN Affectation A ON P.id_affectation = A.id_affectation
            LEFT JOIN Visite v ON P.id_visite = v.id_visite
            WHERE v.VE_OMSI = '{selected_date}'
        """
        cursor.execute(query)

        employees = cursor.fetchall()


        return employees
    
if __name__ == '__main__':

    model = Employee_VEOMSI_Model("data\my_database.sqlite")


    date = "sam. nov. 25 2023"
    result = model.get_employees_for_date(date)
    for results in result:
        print(results)