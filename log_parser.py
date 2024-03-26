import os
from datetime import datetime

# Function to parse the log file and return connections
def parse_log_file(file_path):
    connections = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()  # Splitting each line into parts
                timestamp = int(parts[0]) / 1000  # Extracting and converting timestamp from milliseconds to seconds
                left_host = parts[1]  # Extracting left host
                right_host = parts[2]  # Extracting right host
                connections.append((timestamp, left_host, right_host))  # Adding connection to list
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)
    return connections

# Function to filter connections based on time range and hostname
def filter_connections(connections, time_init, time_end, hostname):
    try:
        time_init = datetime.strptime(time_init, '%Y-%m-%d %H:%M:%S').timestamp()
        time_end = datetime.strptime(time_end, '%Y-%m-%d %H:%M:%S').timestamp()
    except ValueError:
        print("Error: Invalid datetime format.")
        exit(1)
    
    filtered_connections = []
    # Iterating through connections and filtering based on criteria
    for timestamp, left_host, right_host in connections:
        if time_init <= timestamp <= time_end and (left_host == hostname or right_host == hostname):
            filtered_connections.append((left_host, right_host))  # Adding filtered connection to list
    return filtered_connections

# Main function to execute the script
def main():
    file_path = input("Enter the path to the log file: ") #input("input-file-10000")  Path to the log file
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        exit(1)
    time_init = input("Enter the start datetime (YYYY-MM-DD HH:MM:SS): ")  # Start datetime input
    time_end = input("Enter the end datetime (YYYY-MM-DD HH:MM:SS): ")  # End datetime input
    hostname = input("Enter the hostname: ")  # Hostname input

    connections = parse_log_file(file_path)  # Parsing log file to get connections
    filtered_connections = filter_connections(connections, time_init, time_end, hostname)  # Filtering connections

    # Create a folder named 'result' if it doesn't exist
    result_folder = 'results'
    os.makedirs(result_folder, exist_ok=True)

    # Write filtered connections to a file
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_file_name = f"{result_folder}/{hostname}_{current_time}.txt"
    with open(output_file_name, 'w') as f:
        for connection in filtered_connections:
            connection_str = f"{connection[0]} -> {connection[1]}\n"
            f.write(connection_str)
            print(connection_str.strip())

    print(f"Result saved to {output_file_name}")

# Entry point of the script
if __name__ == "__main__":
    main()
