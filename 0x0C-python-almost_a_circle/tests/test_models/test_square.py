#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    Unittest for Square class
    """
    def test_setter_with_wrong_datatypes(self):
        """
        Unittest testing with wrong datadtypes
        """
        with self.assertRaises(TypeError):
            s1 = Square('a')
        with self.assertRaises(TypeError):
            s2 = Square([1, 5, 8, 2])
        with self.assertRaises(TypeError):
            s3 = Square({'a': 5, 'b': 2, 'c': 5})

    def test_setter_with_wrong_int_values(self):
        """
        Unittest testing with wrong datadtypes
        """
        with self.assertRaises(ValueError):
            s4 = Square(0)
        with self.assertRaises(ValueError):
            s5 = Square(-5)

    def test_area_method(self):
        """
        Unittest testing the area method
        """
        s6 = Square(5)
        self.assertEqual(s6.area(), 25)

    def test_display_method_without_coordinates(self):
        """
        Unittest of the display method without coordinates
        """
        s7 = Square(2)
        sys.stdout = StringIO()
        s7.display()
        expected_output = "##\n##\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)
        sys.stdout = sys.__stdout__

    def test_display_method_with_coordinates(self):
        """
        Unittest of the display method with coordinates
        """
        s8 = Square(2, x=1, y=1)
        sys.stdout = StringIO()
        s8.display()
        expected_output = "\n ##\n ##\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)
        sys.stdout = sys.__stdout__

    def test_update_method(self):
        """Unittest testing the update method"""
        s9 = Square(5)
        s9.update(10)
        self.assertEqual(s9.id, 10)
        output = s9.__str__()
        self.assertEqual(output, "[Square] (10) 0/0 - 5")
        s9.update(3, 2)
        output = s9.__str__()
        self.assertEqual(output, "[Square] (3) 0/0 - 2")
        s9.update(6, 8, 3, 2)
        self.assertEqual(s9.id, 6)
        self.assertEqual(s9.x, 3)
        output = s9.__str__()
        self.assertEqual(output, "[Square] (6) 3/2 - 8")

    def test_str_method(self):
        """
        Unittest of the __str__ method
        """
        s10 = Square(3, 3)
        output = s10.__str__()
        self.assertEqual(output, "[Square] (9) 3/0 - 3")

    def test_to_dictionary_method(self):
        """Unittest testing the t0_dictionary method"""
        s11 = Square(5)
        d = s11.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['size'], 5)
        self.assertEqual(d['x'], 0)
        self.assertEqual(d['y'], 0)


if __name__ == "__main__":
    unittest.main()
