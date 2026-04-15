"""
cli.py

Command-line interface helpers for displaying CIDR calculator results.
"""

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