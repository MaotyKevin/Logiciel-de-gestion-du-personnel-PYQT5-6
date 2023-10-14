#db_handler.py

import sqlite3

class DatabaseHandler:
    def __init__(self, db_file="data/my_database.sqlite"):
        try:
            self.connection = sqlite3.connect(db_file)
            print("Database connected")
        except sqlite3.Error as err:
            print("Database connection error:", err)
            self.connection = None

    def validate_credentials(self, Username, Password):
        if not self.connection:
            return False  # Return False if there's no valid database connection
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Admin WHERE Username = ? AND Password = ?"
            cursor.execute(query, (Username, Password))
            result = cursor.fetchone()
            cursor.close()

            if result:
                print("Login successiful")
                return True
            else:
                print("Login error")
                return False
        except sqlite3.Error as err:
            print("Error:", err)
            return False

    def close(self):
        if self.connection:
            self.connection.close()
