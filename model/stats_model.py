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
    
if __name__ == '__main__':
    model = Stats_model("data\my_database.sqlite")    
    datas = model.display_donut_chart_team()
    print(datas)