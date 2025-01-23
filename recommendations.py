class RecommendationGenerator:
    def generate_recommendations(self, feasibility_score):
        if feasibility_score >= 8:
            return "Consider seeking investment and focus on scaling your operations."
        elif feasibility_score >= 5:
            return "Conduct more market research and refine your business model."
        else:
            return "Reassess your business idea and consider pivoting your approach."