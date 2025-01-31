from database_handler import DatabaseHandler

def main():
    db_handler = DatabaseHandler()
    db_handler.execute_sql_file('data/business_ideas.sql')
    print("Business ideas loaded successfully.")
    db_handler.close()

if __name__ == "__main__":
    main()