import json
import os
import subprocess
from src.machine import Machine
from src.logger import logger

def get_user_input():
    machines = []
    logger.info("=== DevOps Infrastructure Provisioning Simulator Started ===")
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
    logger.info("Triggering automated service deployment script...")
    print("\n[INFO] Triggering automated service deployment script...")
    try:
        result = subprocess.run(["./scripts/deploy_service.sh"], check=True, text=True, capture_output=True)
        print(result.stdout)
        logger.info("Bash deployment completed successfully.")
        print("[INFO] Bash deployment completed successfully.")
    except subprocess.CalledProcessError as e:
        error_msg = f"Deployment script failed: {e}"
        logger.error(error_msg)
        print(f"[ERROR] {error_msg}")

def main():
    instances = get_user_input()
    
    if instances:
        os.makedirs("configs", exist_ok=True)
        config_path = "configs/instances.json"
        with open(config_path, "w") as f:
            json.dump(instances, f, indent=4)
        
        success_msg = f"Configurations successfully saved to {config_path}"
        logger.info(success_msg)
        print(f"[INFO] {success_msg}")
        
        # Execute bash automation script
        trigger_bash_deployment()
        logger.info("=== Provisioning Process Completed Successfully ===")
    else:
        logger.warning("No machines were added by the user.")
        print("[INFO] No machines were added.")

if __name__ == "__main__":
    main()
