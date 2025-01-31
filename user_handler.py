import mysql
from database_handler import DatabaseHandler

class UserHandler:
    def __init__(self):
        self.db_handler = DatabaseHandler()

    def register_user(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")
        password = input("Enter password: ")
        
        try:
            self.db_handler.register_user(username, email, phone_number, password)
            print("User  registered successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if self.db_handler.login_user(username, password):
            print("Login successful!")
            return username
        else:
            print("Login failed! Please check your username and password.")
            return None

    def get_user_data(self, username):
        user_data = self.db_handler.get_user_data(username)
        if user_data:
            print(f"Username: {user_data[1]}, Email: {user_data[2]}, Phone: {user_data[3]}")
        else:
            print("User  not found.")