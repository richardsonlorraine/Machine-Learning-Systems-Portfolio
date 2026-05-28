class TroubleshootingAgent:
    def __init__(self):
        self.knowledge_base = {
            "wifi": "Restart your router and check the ISP status page.",
            "laptop_overheating": "Check for blocked vents and close background apps.",
            "login_failure": "Verify credentials or trigger a password reset."
        }

    def process_query(self, user_query, sentiment_score):
        query_clean = user_query.lower()
        
        # 1. Prioritize critical human escalation paths based on sentiment data
        if sentiment_score < 0.4:
            return "ESCALATE: High priority user frustration detected. Transferring to manager."
        
        # 2. Multi-intent matching array with a safe fallback default
        intent = None
        if "internet" in query_clean or "wifi" in query_clean:
            intent = "wifi"
        elif "overheating" in query_clean or "hot" in query_clean or "fan" in query_clean:
            intent = "laptop_overheating"
        elif "login" in query_clean or "password" in query_clean:
            intent = "login_failure"
            
        # 3. Safe resolution logic
        if intent and intent in self.knowledge_base:
            return f"Suggested Solution: {self.knowledge_base[intent]}"
        
        return "Suggested Solution: I need more details. Could you specify if the issue is regarding your connection, hardware, or account login?"
