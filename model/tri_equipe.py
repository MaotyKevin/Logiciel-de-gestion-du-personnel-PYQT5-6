import sqlite3

# Connectez-vous à la base de données SQLite
conn = sqlite3.connect('data/my_database.sqlite')
cursor = conn.cursor()

# Exécutez une requête SQL pour récupérer les personnels triés par équipe
query = '''
    SELECT Personnel.badge, Personnel.nom, Equipe.nom_equipe
    FROM Personnel
    INNER JOIN Equipe ON Personnel.id_equipe = Equipe.id_equipe
    ORDER BY Equipe.nom_equipe
'''

cursor.execute(query)

# Récupérez les résultats de la requête
result = cursor.fetchall()

# Affichez les personnels triés par équipe
current_equipe = None
for row in result:
    badge, nom, nom_equipe = row
    if nom_equipe != current_equipe:
        print(f"Équipe : {nom_equipe}")
        current_equipe = nom_equipe
    print(f"Badge : {badge}, Nom : {nom}")

# Fermez la connexion à la base de données
conn.close()
