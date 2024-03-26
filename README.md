# Log Parser

This script parses a log file and filters connections based on a specified time range and hostname.

## Installation

1. Clone this repository to your local machine.
2. Install Python if you haven't already.
3. Install dependencies using `pip install -r requirements.txt`.

## Usage

Run the script by executing the following command:

```bash
python log_parser.py
```

## Saving Results

The script saves the filtered connections in a file inside a folder named "results". The name of each output file is based on the name of the host and the timestamp.

## Example Inputs

- Enter the path to the log file: input-file-10000.txt
- Enter the start datetime (YYYY-MM-DD HH:MM:SS): 2012-01-01 00:10:00
- Enter the end datetime (YYYY-MM-DD HH:MM:SS): 2023-01-01 00:10:00
- Enter the hostname: Mystee

## Notes

- The script correctly parse the log file, filter connections based on the provided time range and hostname, and print the filtered connections.
- The code is reasonably well-designed with separate functions for parsing and filtering connections, making it modular and easier to understand.
- The code has error handling for cases like invalid datetime inputs or file not found.
- The code is relatively easy to extend or maintain due to its modular structure. 
- Additional functionalities or improvements can be made by modifying or adding functions as needed.
- The code is easy to comprehend due to descriptive function and variable names, as well as well-commented sections explaining the purpose of each part of the code.
- The performance would depend on the size of the log file and the number of connections within the specified time range. For large files or extensive time ranges, the performance might degrade, especially since it iterates through all connections linearly. 
However, for typical log file sizes, it should perform adequately. 
- Further optimization could be considered if performance becomes a concern, such as using data structures like dictionaries or sets for faster lookups.
- My script uses only the standard library (datetime, os), there are no external dependencies to include in the requirements.txt. However, if you later decide to use additional libraries, you can list them in provided requirements.txt.


# Log Generator

Included in this repository is a Python script named `log_generator.py` that allows you to generate sample log files containing network connection data. This can be useful for testing the log monitoring script (`log_monitor.py`) with different scenarios and volumes of data.

## Usage

1. Ensure you have Python installed on your system.
2. Navigate to the directory containing the `log_generator.py` script.
3. Run the script with the following command:

    ```
    python log_generator.py <number_of_lines>
    ```

    Replace `<number_of_lines>` with the desired number of lines you want the log file to contain.

## Example

To generate a sample log file with 1000 lines, run the following command:

```
python .\log_generator.py 1000
```

# Log Monitor Script

This Python script monitors log files for network connections and generates hourly reports based on the connections involving a specified target host.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download the repository.
3. Navigate to the directory containing the `log_monitor.py` script.
4. Run the script with the following command:

    ```
    python log_monitor.py <log_file_name> <target_host>
    ```

    Replace `<log_file_name>` with the name of the log file to monitor (e.g., `log_2024-03-26_22-30-51.log`) and `<target_host>` with the hostname you want to monitor connections for (e.g., `host5`).

## Sample Log File

A sample log file (`log_2024-03-26_22-30-51.log`) is provided in the `log_files` directory. This file contains simulated network connections between hosts, timestamped on March 26, 2024, at 22:30:51.

## Expected Result

After running the script with the specified log file name and target host, you should receive an hourly report similar to the following:

```
Hourly report for 2024-03-26 23:00:37:
Hostnames connected to host5: host6, host10, host3, host5, host7, host2, host8, host1, host4, host9
Hostnames received connections from host5: host10, host6, host3, host7, host2, host8, host1, host4, host9
Hostname with the most connections: host2
```
This report provides details on hostnames connected to the specified target host, hostnames receiving connections from the target host, and the hostname with the most connections to the target host during the last hour.
