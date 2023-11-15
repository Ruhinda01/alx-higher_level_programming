#!/usr/bin/python3
"""unittest for the base class"""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    def test_to_json_string_returns_empty_string(self):
        b = Base()
        new_list = []
        jd = b.to_json_string(new_list)
        self.assertEqual(jd, "[]")

    def test_to_json_string_returns_json_string(self):
        b = Base()
        new_list = [
                {'id' : 5, 'width' : 10, 'height' : 5}
                ]
        jd = b.to_json_string(new_list)
        self.assertIsInstance(jd, str)
        self.assertEqual(jd, json.dumps(new_list))

    def test_save_to_file(self):
        b = Base()
        b.save_to_file([])
        filename = 'Base.json'
        with open(filename, encoding='utf-8') as f:
            fd = f.read()
        self.assertEqual(fd, "[]")


if __name__ == '__main__':
    unittest.main()
        
