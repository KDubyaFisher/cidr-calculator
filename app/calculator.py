"""
calculator.py

Core IPv4 CIDR parsing and validation logic.
"""


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