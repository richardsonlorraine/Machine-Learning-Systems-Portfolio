import json
import datetime

kb = {
    "slow_internet": {
        "solution": "Performing an automated network stack reset.",
        "risk_level": "low"
    }
}

def execute_safe_fix(intent):
    # Safe lookup: protects against KeyError
    action_item = kb.get(intent)
    if not action_item:
        print(f"WARNING: Intent '{intent}' not mapped to knowledge base operations.")
        return False
        
    if action_item.get("risk_level") == "low":
        print(f"ACTION: {action_item['solution']}")
        return True
    return False
