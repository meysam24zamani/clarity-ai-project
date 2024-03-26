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
