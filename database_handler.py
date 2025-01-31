import mysql.connector
from config import DB_CONFIG
from auth import Auth  # Import the Auth class

class DatabaseHandler:
    def __init__(self):
        self.connection = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create table for business evaluations
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS business_evaluations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            startup_name VARCHAR(255) NOT NULL,
            market_size DECIMAL(10, 2) NOT NULL,
            competition_level INT NOT NULL,
            team_experience INT NOT NULL,
            regulatory_score INT NOT NULL,
            capital_requirements DECIMAL(10, 2) NOT NULL,
            feasibility_score DECIMAL(10, 2),
            recommendations TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Create table for users
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            phone_number VARCHAR(20),
            password VARCHAR(255) NOT NULL
        )
        """)
        self.connection.commit()

    def register_user(self, username, email, phone_number, password):
        # Hash the password using the Auth class
        hashed_password = Auth.hash_password(password)
        self.cursor.execute("""
        INSERT INTO users (username, email, phone_number, password) 
        VALUES (%s, %s, %s, %s)
        """, (username, email, phone_number, hashed_password))
        self.connection.commit()

    def login_user(self, username, password):
        self.cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = self.cursor.fetchone()
        if result and Auth.verify_password(result[0], password):  # Use Auth class for verification
            return True
        return False

    def get_user_data(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        return self.cursor.fetchone()

    def insert_business_evaluation(self, evaluation_data):
        self.cursor.execute("""
        INSERT INTO business_evaluations 
        (startup_name, market_size, competition_level, team_experience, regulatory_score, capital_requirements, feasibility_score, recommendations) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (evaluation_data['startup_name'], evaluation_data['market_size'], evaluation_data['competition_level'],
              evaluation_data['team_experience'], evaluation_data['regulatory_score'], evaluation_data['capital_requirements'],
              evaluation_data['feasibility_score'], evaluation_data['recommendations']))
        self.connection.commit()

    def execute_sql_file(self, file_path):
        with open(file_path, 'r') as file:
            sql_script = file.read()
            for statement in sql_script.split(';'):
                if statement.strip():
                    self.cursor.execute(statement)
            self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()