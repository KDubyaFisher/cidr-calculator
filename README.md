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
