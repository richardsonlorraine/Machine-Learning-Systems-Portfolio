knowledge_base = {"restart": "Please power cycle your router for 30 seconds.", "cables": "Check that the Ethernet cable is clicked into the WAN port.", "isp": "No local issues detected. Contact your ISP support line."} # --- PHASE 2: Diagnostic Reasoning (The 'Think' Layer) ---
def start_diagnostic():
    print("--- AI Diagnostic Agent Active ---")    # Percept 1: Router Status
    if input("Is the router power light on? (y/n): ").lower() == "n":
        print(f"FIX: {knowledge_base['restart']}")
        return    # Percept 2: Physical Layer
    if input("Are cables securely connected? (y/n): ").lower() == "n":
        print(f"FIX: {knowledge_base['cables']}")
        return    # Fallback: External Escalation
    print(f"FIX: {knowledge_base['isp']}") # --- PHASE 3: Intent Recognition (The 'Perceive' Layer) ---
user_query = input("Describe your issue: ").lower()
if "network" in user_query or "internet" in user_query:
    start_diagnostic()
else:
    print("I am currently only trained for network troubleshooting.")