import json
import os
import subprocess
from src.machine import Machine

def get_user_input():
    machines = []
    print("=== DevOps Infrastructure Provisioning Simulator ===")
    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os_name = input("Enter OS (Ubuntu/CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")
        
        machine = Machine(name, os_name, cpu, ram)
        machine.log_creation()
        machines.append(machine.to_dict())
        
    return machines

def trigger_bash_deployment():
    print("\n[INFO] Triggering automated service deployment script...")
    try:
        result = subprocess.run(["./scripts/deploy_service.sh"], check=True, text=True, capture_output=True)
        print(result.stdout)
        print("[INFO] Bash deployment completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Deployment script failed: {e}")

def verify_configuration_file(filepath):
    print(f"\n[INFO] Verifying existence of configuration file: {filepath}")
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"[SUCCESS] File verified! Path: {filepath}, Size: {size} bytes.")
    else:
        print(f"[WARNING] Configuration file not found at {filepath}.")

def main():
    instances = get_user_input()
    
    if instances:
        config_path = "configs/instances.json"
        with open(config_path, "w") as f:
            json.dump(instances, f, indent=4)
        print(f"[INFO] Configurations successfully saved to {config_path}")
        
        # Run our new verification step
        verify_configuration_file(config_path)
        
        # Execute bash automation script
        trigger_bash_deployment()
    else:
        print("[INFO] No machines were added.")

if __name__ == "__main__":
    main()
