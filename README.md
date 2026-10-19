This is a modular Python-based automation tool that simulates infrastructure provisioning and service configuration. It allows users to define virtual machines dynamically, validates input, stores configurations in a JSON file, and automatically triggers a Bash script to handle deployment while maintaining comprehensive logs.
## Features
- **Interactive Python Simulator:** Prompts user for VM specifications (Name, OS, CPU, RAM).
- **Object-Oriented Design:** Utilizes a dedicated `Machine` class for modular management.
- **Data Persistence:** Automatically saves configuration details to `configs/instances.json`.
- **Bash Automation via Subprocess:** Triggers deployment scripts securely from Python.
- **Advanced Logging & Error Handling:** Captures all events, successes, and errors into `logs/provisioning.log` using Python's `logging` module.

## Execution Instructions
1. Run the main Python simulator:
   ```bash
   python3 infra_simulator.py
