import sqlite3

def get_personnel_by_team(self, team_name):
    try:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()


        query = f'''
                SELECT P.Badge, P.Nom, E.nom_equipe, COALESCE(A.Categorie, 'Aucun') AS Categorie, COALESCE(A.Fonction, 'Aucun') AS Fonction, COALESCE(S.sousCategorie, 'Aucun') AS sousCategorie
                FROM Personnel P
                LEFT JOIN Affectation A ON P.id_affectation = A.id_affectation
                LEFT JOIN SousCategorie S ON A.id_sousCategorie = S.id_sousCategorie
                LEFT JOIN Equipe E ON P.id_equipe = E.id_equipe
                WHERE E.nom_equipe = '{team_name}'  -- Filter by the selected team
                ORDER BY E.nom_equipe
            '''

        cursor.execute(query)
        result = cursor.fetchall()

        conn.close()

        return result

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None
