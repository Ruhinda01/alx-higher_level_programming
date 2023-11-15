#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def test_setters_with_exceptions_wrong_datatypes(self):
        """unittest testing of setters with TypeError (exceptions)"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, '5')
        with self.assertRaises(TypeError):
            r2 = Rectangle('10', 4)
        with self.assertRaises(TypeError):
            r3 = Rectangle(5, 6, [1, 5, 6])
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 5, 2, (1, 4, 8))

    def test_setters_with_exceptions_value_errors(self):
        """unittest testing of setters with ValueError (exceptions)"""
        with self.assertRaises(ValueError):
            r5 = Rectangle(4, -4)
        with self.assertRaises(ValueError):
            r6 = Rectangle(0, 4)
        with self.assertRaises(ValueError):
            r7 = Rectangle(5, 6, -6)
        with self.assertRaises(ValueError):
            r8 = Rectangle(10, 5, 2, -4)

    def test_values_initiated_for_attributes(self):
        """unittest testing values of attributes"""
        r9 = Rectangle(5, 4)
        self.assertEqual(r9.width, 5)
        self.assertEqual(r9.height, 4)
        self.assertEqual(r9.x, 0)
        self.assertEqual(r9.y, 0)

    def test_area_method(self):
        """unittest testing the area method"""
        r10 = Rectangle(5, 4)
        self.assertEqual(r10.area(), 20)

    def test_display_method_without_coordinates(self):
        """Unittest of the display method without coordinates"""
        r11 = Rectangle(3, 2)
        sys.stdout = StringIO()
        r11.display()
        expected_output = "###\n###\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_display_method_with_coordinates(self):
        """Unittest of the display method with coordinates"""
        r12 = Rectangle(3, 2, x=2, y=1)
        sys.stdout = StringIO()
        r12.display()
        expected_output = "\n  ###\n  ###\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_str_method(self):
        """Unittest of the __str__ method"""
        r13 = Rectangle(3, 3)
        output = r13.__str__()
        self.assertEqual(output, "[Rectangle] (12) 0/0 - 3/3")
        r14 = Rectangle(5, 4, x=2, y=4, id=56)
        output = r14.__str__()
        self.assertEqual(output, "[Rectangle] (56) 2/4 - 5/4")

    def test_update_method(self):
        """Unittest testing the update method"""
        r15 = Rectangle(5, 4)
        r15.update(10)
        self.assertEqual(r15.id, 10)
        output = r15.__str__()
        self.assertEqual(output, "[Rectangle] (10) 0/0 - 5/4")
        r15.update(3, 2)
        output = r15.__str__()
        self.assertEqual(output, "[Rectangle] (3) 0/0 - 2/4")
        r15.update(6, 8, 3, 2, 1)
        self.assertEqual(r15.id, 6)
        self.assertEqual(r15.x, 2)
        output = r15.__str__()
        self.assertEqual(output, "[Rectangle] (6) 2/1 - 8/3")

    def test_update_args_kwargs_method(self):
        """Unittest testing the update method with args and kwargs"""
        r16 = Rectangle(6, 8)
        r16.update(height=7, x=3, y=5, id=56)
        output = r16.__str__()
        self.assertEqual(output, "[Rectangle] (56) 3/5 - 6/7")

    def test_to_dictionary_method(self):
        """Unittest testing the t0_dictionary method"""
        r17 = Rectangle(10, 2, 1, 9)
        d = r17.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)
        self.assertEqual(d['x'], 1)
        self.assertEqual(d['y'], 9)


if __name__ == '__main__':
    unittest.main()
