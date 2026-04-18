"""
test_calculator.py

Unit tests for CIDR calculator core logic.
"""

import unittest

from app.calculator import (
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



if __name__ == "__main__":
    unittest.main()