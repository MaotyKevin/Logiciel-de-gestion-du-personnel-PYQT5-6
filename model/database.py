#model/database.py

import sqlite3
from PIL import Image
import io

class Databases:
    def __init__(self , db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def recuperer_id_categorie(self,categorie):
        try:
            self.cursor.execute("SELECT id_categorie FROM Categorie WHERE nom_categorie = ?" , (categorie,))
            row = self.cursor.fetchone()
            if row :
                return row[0]
            else :
                return None
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération de l'ID de la categorie : {str(e)}")
            return None

    def recuperer_id_equipe(self,equipe):
        try:
            self.cursor.execute("SELECT id_equipe FROM Equipe WHERE nom_equipe = ?" , (equipe,))
            row = self.cursor.fetchone()
            if row :
                return row[0]
            else :
                return None
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération de l'ID de l'equipe : {str(e)}")
            return None
        
    def recuperer_id_sous_categorie(self, sous_categorie):
        try:
         
            self.cursor.execute("SELECT id_sousCategorie FROM SousCategorie WHERE sousCategorie = ?", (sous_categorie,))
            row = self.cursor.fetchone()
            if row:
                return row[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération de l'ID de sous-catégorie : {str(e)}")
            return None
        
    def recuperer_donnees_categorie(self):
        try:
            
            self.cursor.execute("SELECT nom_categorie FROM Categorie")
            categorie_data = [row[0] for row in self.cursor.fetchall()]
            return categorie_data
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données de categorie : {str(e)}")
            return []    


    def recuperer_donnees_equipe(self):
        try:
            
            self.cursor.execute("SELECT nom_equipe FROM Equipe")
            equipe_data = [row[0] for row in self.cursor.fetchall()]
            return equipe_data
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données d'équipe : {str(e)}")
            return []

    def recuperer_donnees_sous_categorie(self):
        try:
          
            self.cursor.execute("SELECT sousCategorie FROM SousCategorie")
            sous_categorie_data = ["Aucun"]  # Option "Aucun"
            sous_categorie_data += [row[0] for row in self.cursor.fetchall()]
            return sous_categorie_data
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données de sous-catégorie : {str(e)}")
            return []

    def inserer_visite(self, du, date_visite_medicale, date_accueil_securite, msb, consignation, ms, ve_omsi):
        # Insérer les données dans la table "Visite" et récupérer l'ID inséré
        insert_query = """
            INSERT INTO Visite (DU, DateVisiteMedicale, DateAccueilSecurite, MSB, Consignation, MS, VE_OMSI)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(insert_query, (du, date_visite_medicale, date_accueil_securite, msb, consignation, ms, ve_omsi))
        self.connection.commit()
        return self.cursor.lastrowid

    def inserer_affectation(self, fonction, deuxieme_fonction, date_debut, date_fin, cause_depart,id_categorie, id_sous_categorie):
        # Insérer les données dans la table "Affectation" et récupérer l'ID inséré
        insert_query = """
            INSERT INTO Affectation (Fonction, DeuxiemeFonction, DateDebut, DateFin, CauseDepart,id_categorie, id_sousCategorie)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(insert_query, (fonction, deuxieme_fonction, date_debut, date_fin, cause_depart,id_categorie, id_sous_categorie))
        self.connection.commit()
        return self.cursor.lastrowid

    def inserer_equipement(self, date_equipement, casque, haut, lunette, chaussure):
        # Insérer les données dans la table "Equipement" et récupérer l'ID inséré
        insert_query = """
            INSERT INTO Equipement (DateEquipement, Casque, Haut, Lunette, Chaussure)
            VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(insert_query, (date_equipement, casque, haut, lunette, chaussure))
        self.connection.commit()
        return self.cursor.lastrowid

    def inserer_personnel(self, badge, nom, prenom, sexe , cin, date_cin, lieu_cin, contact, date_naissance, lieu_naissance, adresse, photo_data, affectation_id, id_equipe, id_equipement, id_visite):
        # Insérer les données dans la table "Personnel"
        insert_querys = """
            INSERT INTO Personnel (Badge, Nom, Prenom, Sexe , CIN, Date_CIN, Lieu_CIN, Contact, Date_Naissance, Lieu_Naissance, Adresse, Photo, id_affectation, id_equipe, id_equipement, id_visite)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(insert_querys, (badge, nom, prenom, sexe , cin, date_cin, lieu_cin, contact, date_naissance, lieu_naissance, adresse, photo_data, affectation_id, id_equipe, id_equipement, id_visite))
        self.connection.commit()

    def recuperer_personnel(self):
        select_query = """
            SELECT P.Badge, P.Nom, P.Prenom, P.CIN, P.Contact,P.Photo, E.nom_equipe,  A.Fonction
            FROM Personnel P
            LEFT JOIN Equipe E ON P.id_equipe = E.id_equipe
            LEFT JOIN Affectation A ON P.id_affectation = A.id_affectation
        """

        try:
            self.cursor.execute(select_query)
            resultats = self.cursor.fetchall()
            return resultats

            """# Convert the photo data from string to bytes
            resultats_with_bytes_photo = []
            for row in resultats:
                badge, nom, prenom, cin,  contact, photo_data, equipe, fonction,  = row
                if photo_data:
                    photo_data_bytes = bytes(photo_data, 'utf-8')  # Assuming the encoding is UTF-8
                else:
                    photo_data_bytes = None
                resultats_with_bytes_photo.append((badge, nom, prenom, cin,contact,photo_data_bytes, equipe,  fonction ))

            return resultats_with_bytes_photo"""
          
            
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données : {e}")

    def afficher_personnel(self):
        # Sélectionnez les colonnes requises de la table "Personnel" et joignez la table "Affectation"
        select_query = """
            SELECT P.Badge, P.Nom, P.Photo, A.Fonction
            FROM Personnel P
            LEFT JOIN Affectation A ON P.id_affectation = A.id_affectation
        """
        
        try:
            self.cursor.execute(select_query)
            resultats = self.cursor.fetchall()
            
            for row in resultats:
                badge, nom, photo_data, affectation = row
                
                print(f"Badge: {badge}")
                print(f"Nom: {nom}")
                print(f"Affectation: {affectation}")
                
                # Affichez la photo à partir des données binaires
                if photo_data:
                    photo = Image.open(io.BytesIO(photo_data))
                    photo.show()
                else:
                    print("Aucune photo disponible.")
                
                print("-" * 40)
                
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données : {e}")

    def effacer_ligne(self , table_name , idname , id_a_supp):
        delete_query = f"DELETE FROM {table_name} WHERE {idname} = ?"

        try:
            self.cursor.execute(delete_query, (id_a_supp,))
            self.connection.commit()
            print(f"Ligne avec l'id {id} supprimée avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression de la ligne : {e}")


    def drop_table(self, table_name):
        # Construct the SQL statement to drop the table
        query = f"DROP TABLE IF EXISTS {table_name}"

        # Execute the query to drop the table
        self.cursor.execute(query)
        self.connection.commit()

    def recup_column(self , nom_table):

        # Récupérez les noms de colonnes de la table spécifiée
        requete_colonnes = f"PRAGMA table_info({nom_table})"
        self.cursor.execute(requete_colonnes)
        resultats_colonnes = self.cursor.fetchall()

        # Créez une liste pour stocker les noms de colonnes
        noms_colonnes = []

        # Remplissez la liste avec les noms de colonnes
        for row in resultats_colonnes:
            nom_colonne = row[1]
            noms_colonnes.append(nom_colonne)
        return noms_colonnes

    def dictionnaire_dynamique(self , noms_colonnes,  valeurs):
        donnees_a_inserer = {}
        for colonne, valeur in zip(noms_colonnes, valeurs):
            donnees_a_inserer[colonne] = valeur
        return donnees_a_inserer
    
    def ajout_valeur(self , noms_colonnes,nom_table , valeurs_a_inserer):
        


        # Créez dynamiquement le dictionnaire de données
        donnees_a_inserer = self.dictionnaire_dynamique(noms_colonnes, valeurs_a_inserer)

        # Construisez la requête INSERT INTO dynamiquement en utilisant les noms de colonnes
        colonnes = ', '.join(noms_colonnes)  # Convertit la liste en une chaîne de noms de colonnes séparés par des virgules
        valeurs = ', '.join(['?'] * len(noms_colonnes))  # Crée une chaîne de '?' correspondant au nombre de colonnes

        requete = f"INSERT INTO {nom_table} ({colonnes}) VALUES ({valeurs})"

        # Exécutez la requête INSERT INTO en utilisant les données à insérer
        valeurs_a_inserer = [donnees_a_inserer[colonne] for colonne in noms_colonnes]
        self.cursor.execute(requete, valeurs_a_inserer)
        self.connection.commit()

    def create_tables(self):
        # Table "Sous Categorie"
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS SousCategorie (
                id_sousCategorie INTEGER PRIMARY KEY,
                sousCategorie TEXT
            )
        """)

        # Table "Equipement"
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Equipement (
                id_equipement INTEGER PRIMARY KEY,
                DateEquipement DATE,
                Casque TEXT,
                Haut TEXT,
                Lunette TEXT,
                Chaussure TEXT
            )
        """)

        # Table "Affectation"
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Affectation (
                id_affectation INTEGER PRIMARY KEY,
                Fonction TEXT,
                DeuxiemeFonction TEXT,
                Categorie TEXT,
                DateDebut DATE,
                DateFin DATE,
                CauseDepart TEXT,
                id_sousCategorie INTEGER,
                FOREIGN KEY (id_sousCategorie) REFERENCES SousCategorie (id_sousCategorie)
            )
        """)

        # Table "Visite"
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Visite (
                id_visite INTEGER PRIMARY KEY,
                DU DATE,
                DateVisiteMedicale DATE,
                DateAccueilSecurite DATE, 
                MSB DATE, 
                Consignation DATE,
                MS DATE,
                VE_OMSI DATE
            )
        """)

        #Table Equipe
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Equipe (
                id_equipe INTEGER PRIMARY KEY,
                nom_equipe TEXT
            )
        """)

        # Table "Personnel"
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Personnel (
                Badge TEXT PRIMARY KEY,
                Nom TEXT,
                Prenom TEXT,
                Sexe TEXT (10),
                CIN TEXT,
                Date_CIN DATE,
                Lieu_CIN DATE,
                Contact TEXT,
                Date_Naissance DATE,
                Lieu_Naissance TEXT,
                Adresse TEXT,
                Photo BLOB,
                id_affectation INTEGER,
                id_equipe INTEGER,
                id_equipement INTEGER,
                id_visite INTEGER,
                FOREIGN KEY (id_affectation) REFERENCES Affectation (id_affectation),
                FOREIGN KEY (id_equipe) REFERENCES Equipe (id_equipe),
                FOREIGN KEY (id_equipement) REFERENCES Equipement (id_equipement),
                FOREIGN KEY (id_visite) REFERENCES Visite (id_visite)
                
            )
        """)

        self.connection.commit()

    def close(self):
        self.connection.close()



 
