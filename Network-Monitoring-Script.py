import subprocess
import time
import json
import sys
from rich.console import Console
from rich.table import Table
from rich.live import Live

# Path to the JSON file
json_file_path = r'\\192.168.1.1\network_address.json'

try:
    # Read addresses and names from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Create a list to store the addresses and names
    addresses = [(entry['Address'], entry['Name'], 0, 0) for entry in data if entry.get('Address') and entry.get('Name')]

except FileNotFoundError:
    print("Error: JSON file not found.")
    print("Using default addresses and names instead.")
    addresses = [
        ('google.com', 'Google', 0, 0),
        ('8.8.8.8', 'Google DNS', 0, 0)
    ]

except Exception as e:
    print(f"Error: Failed to load JSON file - {e}")
    sys.exit(1)

# Function to check the status of an address
def check_address(address):
    try:
        result = subprocess.run(['ping', '-n', '1', '-w', '1000', address], capture_output=True, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error: Ping command returned non-zero exit code - {e}")
        return False
    except Exception as e:
        print(f"Error: Failed to execute ping command - {e}")
        return False

# Create a console object
console = Console()

# Start the pinging process
with Live(console=console, auto_refresh=False) as live:
    while True:
        try:
            # Check internet access
            if not check_address('8.8.8.8'):
                print("Error: No internet access. Please check your network connection.")
                break

            # Create a table object
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("Name")
            table.add_column("Status")
            table.add_column("Connected Count")
            table.add_column("Disconnected Count")

            # Iterate through each address
            for i, (address, name, connected_count, disconnected_count) in enumerate(addresses):
                # Check the status of the address
                status = check_address(address)

                # Update the counters based on the status
                connected_count += status
                disconnected_count += not status

                # Update the counters in the addresses list
                addresses[i] = (address, name, connected_count, disconnected_count)

                # Determine the status text and color
                status_text = "[green]✅ Connected[/green]" if status else "[red]❌ Disconnected[/red]"

                # Add a row to the table
                table.add_row(name, status_text, str(connected_count), str(disconnected_count))

            # Render the table
            console.clear()
            console.print(table)

            # Refresh the console output
            live.refresh()
            print("Press [Ctrl + C] to stop the program.")

            # Wait for 2 seconds before updating the table
            time.sleep(2)

        except KeyboardInterrupt:
            print("\nProgram stopped by the user.")
            sys.exit(0)

        except Exception as e:
            print(f"Error: {e}")
            continue
