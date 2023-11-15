#!/usr/bin/python3
"""unittest for the base class"""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test base class"""
    def test_to_json_string_returns_empty_string(self):
        """unittest Testing to_json_string with empty string"""
        b = Base()
        new_list = []
        jd = b.to_json_string(new_list)
        self.assertEqual(jd, "[]")

    def test_to_json_string_returns_json_string(self):
        """unittest Testing to_json_string with list of dictionary"""
        b = Base()
        new_list = [
                {'id': 5, 'width': 10, 'height': 5}
                ]
        jd = b.to_json_string(new_list)
        self.assertIsInstance(jd, str)
        self.assertEqual(jd, json.dumps(new_list))

    def test_save_to_file_with_empty_list(self):
        """unittest testing save_to_file with empty list"""
        b = Base()
        b.save_to_file([])
        filename = 'Base.json'
        with open(filename, encoding='utf-8') as f:
            fd = f.read()
        self.assertEqual(fd, "[]")

    def test_save_to_file_with_list_of_dictionaries_rect(self):
        """unittest testing save_to_file with Rectangle"""
        r1 = Rectangle(10, 5, 6, 1, 2)
        r2 = Rectangle(11, 8, 5, 3, 2)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', encoding='utf-8') as f:
            fd = json.loads(f.read())
        self.assertIsInstance(fd, list)
        lstd = [
            {'id': 2, 'width': 10, 'height': 5, 'x': 6, 'y': 1},
            {'id': 2, 'width': 11, 'height': 8, 'x': 5, 'y': 3}
        ]
        self.assertEqual(fd, lstd)

    def test_save_to_file_with_list_of_dictionaries_sq(self):
        """unittest testing save_to_file with Square"""
        s1 = Square(4, x=2, y=1, id=2)
        s2 = Square(8, x=4, y=3, id=3)
        Square.save_to_file([s1, s2])
        with open('Square.json', encoding='utf-8') as f:
            fd = json.loads(f.read())
        self.assertIsInstance(fd, list)
        lstd = [
            {'id': 2, 'size': 4, 'x': 2, 'y': 1},
            {'id': 3, 'size': 8, 'x': 4, 'y': 3}
        ]
        self.assertEqual(fd, lstd)

    def test_from_json_string_returns_empty_list(self):
        """unittest testing from_json_string with empty list"""
        b = Base()
        new_list = []
        json_input = b.to_json_string(new_list)
        json_output = b.from_json_string(json_input)
        self.assertEqual(json_output, [])
        self.assertIsInstance(json_output, list)

    def test_from_json_string_returns_list_of_dictionaries(self):
        """unittest testing from_json_string a list of dictionaries"""
        b = Base()
        new_list = [
            {'id': 2, 'size': 4, 'x': 2, 'y': 1},
            {'id': 3, 'size': 8, 'x': 4, 'y': 3}
        ]
        json_input = b.to_json_string(new_list)
        json_output = b.from_json_string(json_input)
        self.assertEqual(json_output, new_list)
        self.assertIsInstance(json_output, list)

    def test_create_method_with_rectangle_class(self):
        """unittest testing create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertNotEqual(r1, r2)

    def test_create_method_with_square_class(self):
        """unittest testing create method"""
        s1 = Square(9, x=2, y=2, id=6)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertNotEqual(s1, s2)

    def test_load_from_file_method_with_Rectangle(self):
        """unittest testing the load from file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(3, 5, 1)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles_output, list)

    def test_load_from_file_method_with_Square(self):
        """unittest testing the load from file method"""
        r1 = Square(10, 7, 2, 8)
        r2 = Square(3, 5, 1)
        list_square_input = [r1, r2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertIsInstance(list_square_output, list)


if __name__ == '__main__':
    unittest.main()
