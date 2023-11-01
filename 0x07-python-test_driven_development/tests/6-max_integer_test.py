#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max integer"""
    def test_function_works(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([2, 1, 4, 2]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            max_integer(None)
        self.assertEqual(max_integer([]), None)

    def test_raises_from_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, "cat", 6, 9])
        with self.assertRaises(TypeError):
            max_integer([6, 5, 8, None])


if __name__ == '__main__':
    unittest.main()
