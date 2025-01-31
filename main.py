import logging
from input_handler import InputHandler
from analysis import FeasibilityAnalyzer
from database_handler import DatabaseHandler
from recommendations import RecommendationGenerator
from user_handler import UserHandler

def setup_logging():
    logging.basicConfig(filename='data/logs/app.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def display_menu():
    print("\nMenu Options:")
    print("1. Check Feasibility Score and Recommendations")
    print("2. Logout")

def admin_menu():
    print("\nAdmin Menu:")
    print("1. Compare User Data")
    print("2. Logout")

def main():
    setup_logging()
    logging.info("Application started.")
    
    user_handler = UserHandler()
    db_handler = DatabaseHandler()
    username = None
    
    while True:
        print("\n1. Admin\n2. Register\n3. Login\n4. Exit")
        action = input("Choose an option: ")

        if action == '1':
            admin_user = input("Enter admin username: ")
            admin_pass = input("Enter admin password: ")
            if admin_user == "shahriar964" and admin_pass == "shahriar":
                print("Admin login successful!")
                while True:
                    admin_menu()
                    admin_choice = input("Select an option: ")
                    if admin_choice == '1':
                        from compare import compare_business_ideas
                        compare_business_ideas()
                    elif admin_choice == '2':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Try again.")
            else:
                print("Invalid admin credentials!")

        elif action == '2':
            user_handler.register_user()
        
        elif action == '3':
            username = user_handler.login_user()
            if username:
                print("Login successful!")
                break
            else:
                print("Login failed! Please try again.")
        
        elif action == '4':
            print("Exiting application.")
            db_handler.close()
            return
        else:
            print("Invalid option. Try again.")

    # Logged-in user menu
    while username:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            input_handler = InputHandler()
            user_input = input_handler.get_user_input()

            analyzer = FeasibilityAnalyzer()
            feasibility_score = analyzer.calculate_feasibility(user_input)

            recommendations = RecommendationGenerator()
            recs = recommendations.generate_recommendations(feasibility_score)

            evaluation_data = {
                'username': username,
                'startup_name': user_input['startup_name'],
                'market_size': user_input['market_size'],
                'competition_level': user_input['competition_level'],
                'team_experience': user_input['team_experience'],
                'regulatory_score': user_input['regulatory_score'],
                'capital_requirements': user_input['capital_requirements'],
                'feasibility_score': feasibility_score,
                'recommendations': recs
            }

            db_handler.insert_business_evaluation(evaluation_data)

            logging.info("Feasibility score calculated: %s", feasibility_score)
            logging.info("Recommendations generated: %s", recs)

            print(f"Feasibility Score: {feasibility_score}")
            print("Recommendations:")
            print(recs)
        
        elif choice == '2':
            print("Logging out...")
            username = None  # Reset username to exit loop

        else:
            print("Invalid option. Try again.")
    
    db_handler.close()

if __name__ == "__main__":
    main()
