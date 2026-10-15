import json
from src.machine import Machine

def get_user_input():
    machines = []
    print("=== DevOps Infrastructure Provisioning Simulator ===")
    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os = input("Enter OS (Ubuntu/CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")
        
        # Create machine instance using our Machine class
        machine = Machine(name, os, cpu, ram)
        machine.log_creation()
        
        machines.append(machine.to_dict())
        
    return machines

def main():
    # Collect data from user
    instances = get_user_input()
    
    # Save configurations to JSON file as required
    if instances:
        with open("configs/instances.json", "w") as f:
            json.dump(instances, f, indent=4)
        print("[INFO] Configurations successfully saved to configs/instances.json")
    else:
        print("[INFO] No machines were added.")

if __name__ == "__main__":
    main()
