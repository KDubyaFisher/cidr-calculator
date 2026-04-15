"""
cli.py

Command-line interface helpers for displaying and running the CIDR calculator.
"""

from app.calculator import calculate_subnet_info, parse_cidr


def print_subnet_info(info) -> None:
    """
    Print subnet calculation results in a clean, readable format.
    """
    print("\n=== CIDR Calculator Results ===")
    print(f"IP Address        : {info.ip_address}")
    print(f"CIDR Prefix       : /{info.cidr}")
    print(f"Subnet Mask       : {info.subnet_mask}")
    print(f"Wildcard Mask     : {info.wildcard_mask}")
    print(f"Network Address   : {info.network_address}")
    print(f"Broadcast Address : {info.broadcast_address}")
    print(f"First Usable IP   : {info.first_usable_address}")
    print(f"Last Usable IP    : {info.last_usable_address}")
    print(f"Total Addresses   : {info.total_addresses}")
    print(f"Usable Hosts      : {info.usable_hosts}")
    print()


def run_cli() -> None:
    """
    Run the interactive command-line subnet calculator.
    """
    print("CIDR Calculator")
    print("Enter an IPv4 address and CIDR prefix.")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        ip_input = input("Enter IPv4 address: ").strip()
        if ip_input.lower() == "q":
            print("Goodbye.")
            break

        cidr_input = input("Enter CIDR (example: /24 or 24): ").strip()
        if cidr_input.lower() == "q":
            print("Goodbye.")
            break

        try:
            cidr = parse_cidr(cidr_input)
            subnet_info = calculate_subnet_info(ip_input, cidr)
            print_subnet_info(subnet_info)
        except ValueError as error:
            print(f"Error: {error}\n")