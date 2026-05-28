# Simple Reflex Logic: Thermostat
def thermostat_agent(current_temp):
    threshold = 20  # 20°C
    if current_temp < threshold:
        return "ACT: Turn on Heater"
    return "ACT: Stay Idle"
    
# Fix: Un-indent Class to Root Level
class WarehouseAgent:
    def __init__(self, agent_id, location):
        self.id = agent_id
        self.location = location  # Current Grid Position
        
    def move(self, target_location, other_agent_loc):  
        # COORDINATION LOGIC: Check for immediate collision
        if target_location == other_agent_loc:
            return f"Agent {self.id}: Conflict detected! Waiting for path to clear."
        self.location = target_location
        return f"Agent {self.id}: Moved to {self.location}"

# Simulation
bot1 = WarehouseAgent("A1", (0, 1))
bot2 = WarehouseAgent("A2", (1, 1))
print(bot1.move(target_location=(1, 1), other_agent_loc=bot2.location))
