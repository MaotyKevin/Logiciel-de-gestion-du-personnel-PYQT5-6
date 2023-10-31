#db_handler.py

import sqlite3

class DatabaseHandler:
    def __init__(self, db_file="data\my_database.sqlite"):
        try:
            self.connection = sqlite3.connect(db_file)
            print("Database connected")
        except sqlite3.Error as err:
            print("Database connection error:", err)
            self.connection = None

    def validate_credentials(self, username, password):
        if not self.connection:
            return None  # Return None if there's no valid database connection
        try:
            cursor = self.connection.cursor()

            # Check the admins table
            query = "SELECT A.Username , R.role FROM Admin A INNER JOIN Role R ON A.id_role = R.id_role WHERE A.Username = ? AND A.Password = ?"
            cursor.execute(query, (username, password))
            admin_result = cursor.fetchone()

            if admin_result:
                AUsername , ARole = admin_result
                # User is an admin
                return AUsername , ARole

            # Check the users table
            query = "SELECT Username , R.role FROM User U INNER JOIN Role R ON U.id_role = R.id_role WHERE U.Username = ? AND U.Password = ?"
            cursor.execute(query, (username, password))
            user_result = cursor.fetchone()

            if user_result:
                Username , URole = user_result
                # User is a regular user
                return Username , URole

            # If no match is found, return None
            return None , None

        except sqlite3.Error as err:
            print("Error:", err)
            return None , None


    def close(self):
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    db_path = 'data\my_database.sqlite'
    handler = DatabaseHandler(db_path)
    result = handler.validate_credentials("MaotyKevin" , "Kev")
    print(f"{result}")
