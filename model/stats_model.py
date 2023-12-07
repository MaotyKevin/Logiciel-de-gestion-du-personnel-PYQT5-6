import sqlite3

class Stats_model:
    def __init__(self, database_name):
        self.database_name = database_name

    def display_donut_chart_team(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT E.nom_equipe, COUNT(P.Badge) as workforce
            FROM Equipe E
            LEFT JOIN Personnel P ON E.id_equipe = P.id_equipe
            GROUP BY E.nom_equipe
        """       
        cursor.execute(query)
        data = cursor.fetchall() 

        return data

    def display_donut_chart_Category(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT C.nom_categorie, COUNT(P.Badge) as workforce
            FROM Categorie C
            LEFT JOIN Affectation A ON C.id_categorie = A.id_categorie
            LEFT JOIN Personnel P ON A.id_affectation = P.id_affectation
            GROUP BY C.nom_categorie
        """       
        cursor.execute(query)
        data = cursor.fetchall() 

        return data
    
    def display_donut_chart_SC(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        query = """
            SELECT SC.sousCategorie, COUNT(P.Badge) as workforce
            FROM SousCategorie SC
            LEFT JOIN Affectation A ON SC.id_sousCategorie = A.id_sousCategorie
            LEFT JOIN Personnel P ON A.id_affectation = P.id_affectation
            GROUP BY SC.sousCategorie
        """       
        cursor.execute(query)
        data = cursor.fetchall() 

        return data
    
if __name__ == '__main__':
    model = Stats_model("data\my_database.sqlite")    
    datas = model.display_donut_chart_SC()
    print(datas)