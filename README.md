# Network Address Monitoring

This script allows you to monitor the connectivity status of network addresses by pinging them periodically. It reads the addresses and names from a JSON file and displays the status in a table using the [rich](https://rich.readthedocs.io/) library.

![Network Monitoring Script](https://raw.githubusercontent.com/saeed205/Network-Monitoring-Script/main/Network-Monitoring-Script.png)

## Prerequisites

- Python 3.6 or later
- `pip` package manager

## Installation

1. Clone the repository or download the script file `network_monitor.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Install the required dependencies by running the following command:

```shell
pip install rich
```

## Usage

1. Create a JSON file (`network_address.json`) containing the addresses and names of the networks you want to monitor. The file should have the following structure:

```json
[
  {
    "Address": "google.com",
    "Name": "Google"
  },
  {
    "Address": "facebook.com",
    "Name": "Facebook"
  },
  {
    "Address": "youtube.com",
    "Name": "YouTube"
  },
  {
    "Address": "microsoft.com",
    "Name": "Microsoft"
  },
  {
    "Address": "amazon.com",
    "Name": "Amazon"
  },
  {
    "Address": "apple.com",
    "Name": "Apple"
  },
  {
    "Address": "twitter.com",
    "Name": "Twitter"
  },
  {
    "Address": "linkedin.com",
    "Name": "LinkedIn"
  },
  {
    "Address": "netflix.com",
    "Name": "Netflix"
  },
  {
    "Address": "instagram.com",
    "Name": "Instagram"
  },
  {
    "Address": "bbc.com",
    "Name": "BBC"
  },
  {
    "Address": "cnn.com",
    "Name": "CNN"
  },
  {
    "Address": "nytimes.com",
    "Name": "The New York Times"
  },
  {
    "Address": "wikipedia.org",
    "Name": "Wikipedia"
  },
  {
    "Address": "instagram.com",
    "Name": "Instagram"
  },
  {
    "Address": "digikala.com",
    "Name": "Digikala"
  },
  {
    "Address": "divar.ir",
    "Name": "Divar"
  },
  {
    "Address": "aparat.com",
    "Name": "Aparat"
  },
  {
    "Address": "varzesh3.com",
    "Name": "Varzesh3"
  },
  {
    "Address": "zoomit.ir",
    "Name": "Zoomit"
  },
  {
    "Address": "digiato.com",
    "Name": "Digiato"
  }
]
```

2. Update the `json_file_path` variable in the script to point to the location of your JSON file:

```python
json_file_path = r'path/to/network_address.json'
```

3. Run the script by executing the following command:

```shell
python network_monitor.py
```

4. The script will start pinging the network addresses and display the status in a table. The table will be updated every 2 seconds.

5. To stop the script, press `Ctrl + C`.

## Example

Here's an example usage of the script:

```python
import subprocess
import time
import json
import sys
from rich.console import Console
from rich.table import Table
from rich.live import Live

# Path to the JSON file
json_file_path = r'\\192.168.1.1\network_address.json'

# ... (code omitted for brevity)
```

In this example, the script imports the necessary modules and sets the `json_file_path` variable to the path of the JSON file containing the network addresses. It then proceeds to read the addresses and names from the JSON file and store them in a list called `addresses`.

Next, the script defines a function `check_address` to ping an address and determine its status. It uses the `subprocess.run` function to execute the ping command and captures the output. If the ping is successful (return code 0), the function returns `True`; otherwise, it returns `False`.

The script creates a `Console` object from the `rich.console` module, which is used for rendering the table and updating the console output. It also initializes a `Live` object, which handles the live updating of the console output.

Inside the main loop, the script checks if there is internet access by calling `check_address` with the Google DNS address. If there is no internet access, an error message is displayed, and the script exits. Otherwise, it continues to create a `Table` object using the `rich.table` module. The table has four columns: "Name," "Status," "Connected Count," and "Disconnected Count."

The script iterates through each address in the `addresses` list and checks its status by calling `check_address`. It updates the counters for connected and disconnected counts and updates the address in the `addresses` list. It also determines the status text and color based on the status.

After updating the table and refreshing the console output, the script waits for 2 seconds before repeating the process. The loop continues until the user interrupts the program by pressing `Ctrl + C`.

## Troubleshooting

- **JSON file not found**: If the JSON file specified in `

json_file_path` is not found, the script will display an error message and use default addresses and names instead. Make sure the file path is correct and the file exists.
- **Failed to load JSON file**: If there is an error while loading the JSON file, such as invalid JSON syntax, the script will display an error message and exit. Check the JSON file for any formatting issues.
- **Ping command error**: If there is an error while executing the ping command, the script will display an error message and continue. Make sure the `ping` command is available in your system's environment variables.
