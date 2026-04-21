"""
cli.py

Command-line interface helpers for displaying and running the CIDR calculator.
"""

from __future__ import annotations

import argparse

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


def build_parser() -> argparse.ArgumentParser:
    """ 
    Build and return the argument parser for the CIDR calculator.
    
    If both --ip and --cidr are provided, the calculator runs in non-interactive mode. If neither is provided, the calculator falls back to interactive mode.
    """

    parser = argparse.ArgumentParser(description="Calculate IPv4 subnet details from an IP address and CIDR prefix.")

    parser.add_argument(
        "--ip",
        help="IPv4 address to calculate against (example: 192.168.1.10).",
    )
    parser.add_argument(
        "--cidr",
        help="CIDR prefix length (example: /24 or 24).",
    )

    return parser


def run_interactive_cli() -> int:
    """
    Run the interactive command-line subnet calculator.

    Returns:
        int: Process exit code.
    """
    print("CIDR Calculator")
    print("Enter an IPv4 address and CIDR prefix.")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        ip_input = input("Enter IPv4 address: ").strip()
        if ip_input.lower() == "q":
            print("Goodbye.")
            return 0

        cidr_input = input("Enter CIDR (example: /24 or 24): ").strip()
        if cidr_input.lower() == "q":
            print("Goodbye.")
            return 0

        try:
            cidr = parse_cidr(cidr_input)
            subnet_info = calculate_subnet_info(ip_input, cidr)
            print_subnet_info(subnet_info)
        except ValueError as error:
            print(f"Error: {error}\n")


def run_non_interactive(ip_input: str, cidr_input: str) -> int:
    """
    Run the CIDR calculator in non-interactive mode.
    
    Args:
        ip_input: The IPv4 address supplied by the user
        cidr_input: The CIDR prefix supplied by the user

    Returns:
        int: Process exit code.        
    """
    try:
        cidr = parse_cidr(cidr_input)
        subnet_info = calculate_subnet_info(ip_input, cidr)
        print_subnet_info(subnet_info)
        return 0
    except ValueError as error:
        print(f"Error: {error}")
        return 1