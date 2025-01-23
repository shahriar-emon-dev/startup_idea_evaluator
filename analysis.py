class FeasibilityAnalyzer:
    def calculate_feasibility(self, user_input):
        score = (user_input['market_size'] / 10) - user_input['competition_level'] + user_input['team_experience']
        score += user_input['regulatory_score']  # Add regulatory score
        score -= user_input['capital_requirements'] / 100  # Normalize capital requirements
        return max(0, min(score, 10))  # Ensure score is between 0 and 10