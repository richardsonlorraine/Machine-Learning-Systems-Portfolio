# Simulated Troubleshooting Agent Logic
class TroubleshootingAgent:
    def __init__(self):
        self.knowledge_base = {"wifi": "Restart your router and check the ISP status page.", "laptop_overheating": "Check for blocked vents and close background apps.", "login_failure": "Verify credentials or trigger a password reset."}
    def process_query(self, user_query, sentiment_score): # 1. Identify Intent (Simplified)
        intent = "wifi" if "internet" in user_query else "laptop_overheating" # 2. Sentiment-Based Prioritization
        # Sentiment score < 0.4 indicates high frustration
        if sentiment_score < 0.4:
            return "ESCALATE: High priority user frustration detected." # 3. Decision Logic & Solution Generation
        solution = self.knowledge_base.get(intent, "I need more details to assist.")
        return f"Suggested Solution: {solution}" # Usage
agent = TroubleshootingAgent() # User is calm (0.8) vs User is frustrated (0.2)
print(agent.process_query("My internet is slow", 0.8))
print(agent.process_query("The wifi is broken again!", 0.2))