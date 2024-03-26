import os
import sys
import random
from datetime import datetime

def generate_log_file(log_folder, num_lines):
    # Create log folder if it doesn't exist
    os.makedirs(log_folder, exist_ok=True)

    # Generate log file name based on current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(log_folder, f"log_{current_time}.log")

    # Generate log entries
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            left_host = f"host{random.randint(1, 10)}"
            right_host = f"host{random.randint(1, 10)}"
            file.write(f"{timestamp} {left_host} {right_host}\n")

    return file_path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_log.py <num_lines>")
        sys.exit(1)

    num_lines = int(sys.argv[1])
    log_folder = "log-files"

    log_file_path = generate_log_file(log_folder, num_lines)
    print(f"Log file generated at {log_file_path} with {num_lines} lines.")
