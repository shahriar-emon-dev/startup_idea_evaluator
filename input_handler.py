class InputHandler:
    def get_user_input(self):
        name = input("Enter your startup name: ")
        market_size = float(input("Enter estimated market size (in millions): "))
        competition_level = int(input("Enter competition level (1-10): "))
        team_experience = int(input("Enter team experience (1-10): "))
        regulatory_score = int(input("Rate the regulatory environment (1-10): "))
        capital_requirements = float(input("Estimated capital requirements (in thousands): "))
        
        return {
            'startup_name': name,
            'market_size': market_size,
            'competition_level': competition_level,
            'team_experience': team_experience,
            'regulatory_score': regulatory_score,
            'capital_requirements': capital_requirements
        }