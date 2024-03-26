import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta

# Function to parse log entries and update connection records
def parse_log_entries(log_file, connections):
    try:
        with open(log_file, 'r') as file:
            # Seek to the last position in the file
            file.seek(0, os.SEEK_END)
            file_size = file.tell()

            # If the file size hasn't changed, no new entries
            if file_size <= connections['file_size']:
                return

            # Read new log entries from the last read position
            file.seek(connections['file_size'])
            for line in file:
                parts = line.strip().split()
                # Skip lines with incomplete entries
                if len(parts) < 4:
                    continue
                timestamp = datetime.strptime(parts[0] + " " + parts[1], '%Y-%m-%d %H:%M:%S')
                left_host = parts[2]
                right_host = parts[3]
                connections['entries'].append((timestamp, left_host, right_host))  # Add entry to connections
            # Update the file size
            connections['file_size'] = file_size
    except FileNotFoundError:
        print("Error: Log file not found.")
        exit(1)

# Function to generate hourly output
def generate_hourly_output(connections, target_host):
    # Get current time and time one hour ago
    current_time = datetime.now()
    one_hour_ago = current_time - timedelta(hours=1)

    # Filter connections for the last hour
    filtered_connections = [(timestamp, left, right) for timestamp, left, right in connections['entries']
                            if timestamp >= one_hour_ago]

    # Analyze connections for the last hour
    connected_to_target = set()  # Hostnames connected to the target host
    received_from_target = set()  # Hostnames received connections from the target host
    connections_count = defaultdict(int)  # Count of connections for each hostname
    for timestamp, left, right in filtered_connections:
        if left == target_host:
            connected_to_target.add(right)
        elif right == target_host:
            received_from_target.add(left)
        connections_count[left] += 1
        connections_count[right] += 1

    # Hostname with the most connections in the last hour
    most_connections_host = max(connections_count, key=connections_count.get)

    # Output results
    print(f"Hourly report for {current_time.strftime('%Y-%m-%d %H:%M:%S')}:")
    print(f"Hostnames connected to {target_host}: {', '.join(connected_to_target)}")
    print(f"Hostnames received connections from {target_host}: {', '.join(received_from_target)}")
    print(f"Hostname with the most connections: {most_connections_host}")

# Main function to continuously monitor the log file
def main(log_file_name, target_host):
    # Specify log folder
    log_folder = "log-files"
    log_file = os.path.join(log_folder, log_file_name)

    # Initialize connections dictionary
    connections = {'entries': [], 'file_size': 0}

    # Continuous monitoring loop
    while True:
        # Parse new log entries
        parse_log_entries(log_file, connections)

        # Check if it's time to generate hourly output (every hour)
        current_time = datetime.now()
        if current_time.minute == 0:
            generate_hourly_output(connections, target_host)

        # Sleep for a minute before checking again
        time.sleep(60)

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python log_monitor.py log_file_name target_host")
        exit(1)

    # Specify log file name and target host from the command line arguments
    log_file_name = sys.argv[1]
    target_host = sys.argv[2]

    # Start monitoring the log file
    main(log_file_name, target_host)
