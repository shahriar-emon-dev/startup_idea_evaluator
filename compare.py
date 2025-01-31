from database_handler import DatabaseHandler

def compare_business_ideas():
    db_handler = DatabaseHandler()
    
    try:
        # Fetch all business evaluations from the database
        db_handler.cursor.execute("SELECT * FROM business_evaluations")
        results = db_handler.cursor.fetchall()

        if not results:
            print("No business ideas found in the database.")
            return

        print("Comparing Business Ideas:")
        for row in results:
            print(f"Startup Name: {row[1]}, Market Size: {row[2]}, Competition Level: {row[3]}, "
                  f"Team Experience: {row[4]}, Regulatory Score: {row[5]}, Capital Requirements: {row[6]}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db_handler.close()

if __name__ == "__main__":
    compare_business_ideas()