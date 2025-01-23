
import logging
from input_handler import InputHandler
from analysis import FeasibilityAnalyzer
from database_handler import DatabaseHandler
from recommendations import RecommendationGenerator

def setup_logging():
    logging.basicConfig(filename='data/logs/app.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    setup_logging()
    logging.info("Application started.")

    db_handler = DatabaseHandler()

    input_handler = InputHandler()
    user_input = input_handler.get_user_input()

    analyzer = FeasibilityAnalyzer()
    feasibility_score = analyzer.calculate_feasibility(user_input)

    recommendations = RecommendationGenerator()
    recs = recommendations.generate_recommendations(feasibility_score)

    # Prepare data for insertion
    evaluation_data = {
        'startup_name': user_input['startup_name'],
        'market_size': user_input['market_size'],
        'competition_level': user_input['competition_level'],
        'team_experience': user_input['team_experience'],
        'regulatory_score': user_input['regulatory_score'],
        'capital_requirements': user_input['capital_requirements'],
        'feasibility_score': feasibility_score,
        'recommendations': recs
    }

    # Insert data into the database
    db_handler.insert_business_evaluation(evaluation_data)

    logging.info("Feasibility score calculated: %s", feasibility_score)
    logging.info("Recommendations generated: %s", recs)

    print(f"Feasibility Score: {feasibility_score}")
    print("Recommendations:")
    print(recs)

    db_handler.close()

if __name__ == "__main__":
    main()