"""
test_calculator.py

Unit tests for CIDR calculator core logic.
"""

import unittest

from app.calculator import (
    calculate_subnet_info,
    parse_cidr,
    cidr_to_subnet_mask,
    ip_to_int,
    int_to_ip,
)

class TestCalculator(unittest.TestCase):

    def test_parse_cidr_accepts_slash_format(self):
        self.assertEqual(parse_cidr("/24"), 24)

    def test_parse_cidr_accepts_plain_number(self):
        self.assertEqual(parse_cidr("16"), 16)

    def test_parse_cidr_rejects_invalid_range(self):
        with self.assertRaises(ValueError):
            parse_cidr("/33")

    def test_parse_cidr_rejects_non_numeric(self):
        with self.assertRaises(ValueError):
            parse_cidr("abc")

    def test_cidr_to_subnet_mask_24(self):
        self.assertEqual(cidr_to_subnet_mask(24), "255.255.255.0")

    def test_cidr_to_subnet_mask_16(self):
        self.assertEqual(cidr_to_subnet_mask(16), "255.255.0.0")

    def test_cidr_to_subnet_mask_0(self):
        self.assertEqual(cidr_to_subnet_mask(0), "0.0.0.0")


    def test_ip_conversion_round_trip(self):
        ip_address = "192.168.1.10"
        converted_ip = int_to_ip(ip_to_int(ip_address))
        self.assertEqual(ip_address, converted_ip)

    def test_ip_to_int_invalid_ip(self):
        with self.assertRaises(ValueError):
            ip_to_int("999.999.999.999")

    def test_calculate_subnet_info_for_24(self):
        result = calculate_subnet_info("192.168.1.10", 24)

        self.assertEqual(result.subnet_mask, "255.255.255.0")
        self.assertEqual(result.wildcard_mask, "0.0.0.255")
        self.assertEqual(result.network_address, "192.168.1.0")
        self.assertEqual(result.broadcast_address, "192.168.1.255")
        self.assertEqual(result.first_usable_address, "192.168.1.1")
        self.assertEqual(result.last_usable_address, "192.168.1.254")
        self.assertEqual(result.total_addresses, 256)
        self.assertEqual(result.usable_hosts, 254)

    def test_calculate_subnet_info_for_31(self):
        result = calculate_subnet_info("10.0.0.1", 31)

        self.assertEqual(result.usable_hosts, 2)
        self.assertEqual(result.first_usable_address, "10.0.0.0")
        self.assertEqual(result.last_usable_address, "10.0.0.1")

    def test_invalid_ip_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_subnet_info("999.168.1.10", 24)



if __name__ == "__main__":
    unittest.main()