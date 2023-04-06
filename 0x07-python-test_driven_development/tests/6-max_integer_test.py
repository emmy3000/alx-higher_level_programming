#!/usr/bin/python3

"""
    Unittest for max_integer([..]).

"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""

    def test_module_docsrting(self):
        """Test module docstring."""
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_list(self):
        """Test empty list."""
        self.assertIsNone(max_integer([]))

    def test_no_args(self):
        """Test no arguments passed to function."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test list with only one number."""
        self.assertEqual(max_integer([1]), 1)

    def test_positive_end(self):
        """Test list with all positive numbers and max at the end."""
        self.assertEqual(max_integer([2, 10, 8, 36, 14, 50]), 50)

    def test_positive_middle(self):
        """Test list with all positive numbers and max in the middle."""
        self.assertEqual(max_integer([2, 10, 8, 360, 14, 50]), 360)

    def test_positive_beginning(self):
        """Test list with all positive numbers and max at the beginning."""
        self.assertEqual(max_integer([200, 10, 8, 36, 14, 50]), 200)

    def test_one_negative(self):
        """Test list with one negative number."""
        self.assertEqual(max_integer([200, 10, 8, -36, 14, 50]), 200)

    def test_all_negative(self):
        """Test list will all negative numbers."""
        self.assertEqual(max_integer([-6, -50, -75, -1, -1000]), -1)

    def test_none(self):
        """Test passing None as argument."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Test list with a non-integer tyoe."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "Hello", 4, 5])


if __name__ == '__main__':
    unittest.main()
