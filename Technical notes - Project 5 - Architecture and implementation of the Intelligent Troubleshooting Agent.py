import json # Corrected Knowledge Base (Pillar: Knowledge Base)
knowledge_base = {"restart_router": "Please restart your router and check if the problem persists.", "reset_settings": "Try resetting your network settings in 'Network Reset'.", "check_cables": "Ensure all network cables are securely connected.", "isp_contact": "Please contact your Internet Service Provider (ISP).", "clear_cache": "Clearing your browser cache may resolve connectivity issues."}
def diagnose_network():
    """Rule-based decision tree (Pillar: Reasoning)"""
    print("\n[Diagnostic Mode] Let's troubleshoot your network.")
    if input("Have you restarted your router? (y/n): ").lower() == 'n':
        print(f"Action: {knowledge_base['restart_router']}")
        return
    if input("Are cables securely connected? (y/n): ").lower() == 'n':
        print(f"Action: {knowledge_base['check_cables']}")
        return
    if input("Is the issue only in the browser? (y/n): ").lower() == 'y':
        print(f"Action: {knowledge_base['clear_cache']}")
    else:
        print(f"Action: {knowledge_base['isp_contact']}")
def automate_fix(issue_type):
    """Simulated tool execution (Pillar: Action)"""
    if issue_type == "network":
        print("\n[Automated Action] Resetting system network stack... Success.")
    else:
        print("\n[Error] No automated fix available for this category.") # --- Main Agent Loop (Pillar: Perception) ---
user_query = input("How can I help you today? ").lower()
if "network" in user_query or "wifi" in user_query:
    diagnose_network()
    automate_fix("network")
else:
    print("I'm sorry, I currently only specialize in network troubleshooting.")