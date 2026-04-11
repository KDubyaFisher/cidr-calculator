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
