# eco-sense-monitor
A Python-based environmental sensor simulator for monitoring soil and water conditions.
import random
import time

def check_environmental_status():
    """
    Mihok-Dev Eco-Sense Module
    Simulates environmental monitoring for ecosystem health.
    """
    # Szimulált adatok: talajnedvesség és tisztaság
    moisture_level = random.randint(20, 80)
    purity_index = random.uniform(0.7, 0.99)
    
    print(f"--- Mihok-Dev Eco-Sense Report ---")
    print(f"Soil Moisture: {moisture_level}%")
    print(f"Water Purity Index: {purity_index:.2f}")

    if moisture_level < 30:
        return "CRITICAL: Regeneration needed. Activating PureLight protocols..."
    else:
        return "STATUS: Ecosystem stable. Monitoring continues."

if __name__ == "__main__":
    status = check_environmental_status()
    print(status)
