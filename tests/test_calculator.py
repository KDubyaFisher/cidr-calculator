"""
test_calculator.py

Unit tests for CIDR calculator core logic.
"""

import unittest

from app.calculator import parse_cidr

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



if __name__ == "__main__":
    unittest.main()