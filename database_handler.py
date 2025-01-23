import mysql.connector
from config import DB_CONFIG

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
        self.connection.commit()

    def insert_business_evaluation(self, evaluation_data):
        self.cursor.execute("""
        INSERT INTO business_evaluations 
        (startup_name, market_size, competition_level, team_experience, regulatory_score, capital_requirements, feasibility_score, recommendations) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (evaluation_data['startup_name'], evaluation_data['market_size'], evaluation_data['competition_level'],
              evaluation_data['team_experience'], evaluation_data['regulatory_score'], evaluation_data['capital_requirements'],
              evaluation_data['feasibility_score'], evaluation_data['recommendations']))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()