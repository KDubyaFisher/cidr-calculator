"""
calculator.py

Core IPv4 CIDR parsing, validation, and subnet calculation logic.
"""

from dataclasses import dataclass


@dataclass
class SubnetInfo:
    """
    Represents the full subnet calculation result for an IPv4 address and CIDR.
    """
    ip_address: str
    cidr: int
    subnet_mask: str
    wildcard_mask: str
    network_address: str
    broadcast_address: str
    first_usable_address: str
    last_usable_address: str
    total_addresses: int
    usable_hosts: int


def validate_cidr(cidr: int) -> None:
    """
    Ensure CIDR is a valid IPv4 prefix (0-32).
    """
    if not isinstance(cidr, int):
        raise ValueError("CIDR must be an integer")
    if cidr < 0 or cidr > 32:
        raise ValueError("CIDR must be between 0 and 32")


def parse_cidr(cidr_input: str) -> int:
    """
    Convert input like '/24' or '24' into an integer.

    Examples:
        '/24' -> 24
        '16' -> 16
    """
    # Remove whitespace and optional slash
    cidr_input = cidr_input.strip().replace("/", "")

    try:
        cidr = int(cidr_input)
    except ValueError as exc:
        raise ValueError(
            "CIDR must be an integer between 0 and 32, such as /24 or 24"
        ) from exc

    validate_cidr(cidr)
    return cidr


def cidr_to_subnet_mask(cidr: int) -> str:
    """
    Convert a CIDR prefix length into a dotted-decimal subnet mask.

    Example:
         24 -> '255.255.255.0'
    """
    validate_cidr(cidr)

    # Build a 32-bit binary mask
    binary_mask = "1" * cidr + "0" * (32 - cidr)

    # Split into 4 octets (8 bits each)
    octets = [binary_mask[i:i + 8] for i in range(0, 32, 8)]

    # Convert binary octets to decimal
    decimal_octets = [str(int(octet, 2)) for octet in octets]

    return ".".join(decimal_octets)


def subnet_mask_to_wildcard(mask: str) -> str:
    """
    Convert a dotted-decimal subnet mask into a wildcard mask.

    Example:
         255.255.255.0 -> 0.0.0.255
    """
    octets = mask.split(".")
    wildcard_octets = [str(255 - int(octet)) for octet in octets]
    return ".".join(wildcard_octets)


def validate_ip(ip_address: str) -> None:
    """
    Validate a dotted-decimal IPv4 address.

    Example valid input:
        192.168.1.10
    """
    parts = ip_address.split(".")

    if len(parts) != 4:
        raise ValueError("IP address must contain exactly 4 octets")

    for part in parts:
        if not part.isdigit():
            raise ValueError("Each IP octet must be numeric")

        octet = int(part)
        if octet < 0 or octet > 255:
            raise ValueError("Each IP octet must be between 0 and 255")


def ip_to_int(ip_address: str) -> int:
    """
    Convert a dotted-decimal IPv4 address into a 32-bit integer.
    """
    validate_ip(ip_address)
    octets = [int(part) for part in ip_address.split(".")]

    return (
        (octets[0] << 24)
        | (octets[1] << 16)
        | (octets[2] << 8)
        | octets[3]
    )


def int_to_ip(value: int) -> str:
    """
    Convert a 32-bit integer into a dotted-decimal IPv4 address.
    """

    return ".".join(str((value >> shift) & 255) for shift in (24, 16, 8, 0))


def calculate_subnet_info(ip_address: str, cidr: int) -> SubnetInfo:
    """
    Calculate subnet details for a given IPv4 address and CIDR prefix.

    Returns:
        SubnetInfo containing:
        - subnet mask
        - wildcard mask
        - network address
        - broadcast address
        - first usable host
        - last usable host
        - total addresses
        - usable hosts
    """

    validate_ip(ip_address)
    validate_cidr(cidr)

    ip_int = ip_to_int(ip_address)

    # Special case: /0 means mask is 0.0.0.0
    if cidr == 0:
        mask_int = 0
    else:
        mask_int = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF

    network_int = ip_int & mask_int
    broadcast_int = network_int | (~mask_int & 0xFFFFFFFF)

    subnet_mask = cidr_to_subnet_mask(cidr)
    wildcard_mask = subnet_mask_to_wildcard(subnet_mask)

    total_addresses = 2 ** (32 - cidr)

    # Handle special cases for /31 and /32
    if cidr == 32:
        usable_hosts = 1
        first_usable = int_to_ip(network_int)
        last_usable = int_to_ip(network_int)
    elif cidr == 31:
        usable_hosts = 2
        first_usable = int_to_ip(network_int)
        last_usable = int_to_ip(broadcast_int)
    else:
        usable_hosts = max(total_addresses - 2, 0)
        first_usable = int_to_ip(network_int + 1)
        last_usable = int_to_ip(broadcast_int - 1)

    return SubnetInfo(
        ip_address=ip_address,
        cidr=cidr,
        subnet_mask=subnet_mask,
        wildcard_mask=wildcard_mask,
        network_address=int_to_ip(network_int),
        broadcast_address=int_to_ip(broadcast_int),
        first_usable_address=first_usable,
        last_usable_address=last_usable,
        total_addresses=total_addresses,
        usable_hosts=usable_hosts,
    )