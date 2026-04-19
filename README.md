# CIDR Calculator

A command-line tool for calculating IPv4 subnet information from an IP address and CIDR prefix.

## Features

- Convert CIDR to subnet mask
- Calculate wildcard mask
- Determine network and broadcast addresses
- Compute usable host range
- Handle edge cases such as /31 and /32
- Interactive CLI interface
- Unit tested core logic

## Technologies Used

- Python 3
- Standard Library ('dataclasses', 'unittest')

## Installation 

Clone the repository:

bash \
git clone https://github.com/KDubyaFisher/cidr-calculator.git \
cd cidr-calculator

## Usage

Run the application:

bash \
python3 main.py

Follow the prompts:

bash \
Enter an IPv4 address: 192.168.1.10 \
Enter CIDR (example: /24 or 24): /24

## Example Output

=== CIDR Calculator Results === \
IP Address: 192.168.1.10 \
CIDR Prefix: /24 \
Subnet Mask: 255.255.255.0 \
Wildcard Mask: 0.0.0.255 \
Network Address: 192.168.1.0 \
Broadcast Address: 192.168.1.255 \
First Usable IP: 192.168.1.1 \
Last Usable IP: 192.168.1.254 \
Total Addresses: 256 \
Usable Hosts: 254


## Project Structure

cidr-calculator/ \
| \
|---app/ \
|  |----caclulator.py # Core subnet logic \
|  |____cli.py # CLI interface \
| \
|---tests/ \
|  |____test_calculator.py # Unit tests \
| \
|---main.py # Entry point \
|___README.md 


## Future Improvements

- Add IPv6 support
- Provide a web-based interface (Flask or FastAPI)
- Add subnetting practice mode for learning
- Export results to CSV or JSON
- Package as an installable CLI tool (pip)