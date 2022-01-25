#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests max_integer"""

    def test_basic_scenary(self):
        """Test function for plain vanilla"""
        self.assertEqual(max_integer([0, 1, 2, 3, 10]), 10)

    def test_negative(self):
        """Test for neg int"""
        self.assertEqual(max_integer([-10, -100, -2]), -2)

    def test_empty_list(self):
        """Test function for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_just_one(self):
        """Test for one only number"""
        self.assertEqual(max_integer([0]), 0)

if __name__ == '__main__':
    unittest.main()
