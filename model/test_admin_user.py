import sqlite3 , logging

def authenticate_user(username, password):
    logging.basicConfig(filename='database_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    # Initialize the connection to the database
    connection = sqlite3.connect('data/my_database.sqlite')
    cursor = connection.cursor()

    user_role = None  # Store the user's role here
    if user_role == 'admin':
        table_name = "Admin"
    elif user_role == 'simple_user':
        table_name = "User"
    else:
        # Handle an unknown role (you can raise an error or return None)
        return None
    stringT = str(table_name)

    # Query the database for user authentication
    query = f"SELECT * FROM {stringT} WHERE Username = ? AND Password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    # Close the database connection
    connection.close()

    if user:
        # Authentication successful
        return user_role, user  # You can return more user-specific information if needed
    else:
        # Authentication failed
        return None

# Example usage:
user_info=authenticate_user("Kevin", "kevinmaoty")
if user_info:
    user_role , user = user_info
    name = user[1]
    print(f"_______{user_role}_______\nWelcome back {name} :)")
else:
    print("NOPE")
