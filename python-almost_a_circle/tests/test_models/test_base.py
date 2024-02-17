#!/usr/bin/python3
"""Unittest for base module."""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests to check functionality of Base class"""

    def setUp(self):
        """Resets the Base class to 0."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test to check id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test to check to_json_string method"""
        d = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        json_d = Base.to_json_string([d])
        self.assertEqual(json_d, json.dumps([d]))

    def test_save_to_file_rectangle(self):
        """Test to check save_to_file method for Rectangle"""
        self.helper_save_to_file(Rectangle, [Rectangle(1, 1)])

    def test_save_to_file_square(self):
        """Test to check save_to_file method for Square"""
        self.helper_save_to_file(Square, [Square(1)])

    def helper_save_to_file(self, cls, list_objs=None):
        cls.save_to_file(list_objs)
        with open(cls.__name__ + ".json", "r") as file:
            self.assertEqual(json.loads(file.read()), [
                obj.to_dictionary() for obj in list_objs])

    def test_from_json_string(self):
        """Test to check from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

    def test_create_rectangle(self):
        """Test to check create method for Rectangle"""
        self.helper_create(Rectangle, 1, 1)

    def test_create_square(self):
        """Test to check create method for Square"""
        self.helper_create(Square, 1)

    def helper_create(self, cls, *args, **dictionary):
        r = cls(*args)
        r.update(**dictionary)
        r_dup = cls.create(**dictionary)
        self.assertFalse(r is r_dup)
        self.assertFalse(r == r_dup)

    def test_load_from_file(cls):
        """Test to check load_from_file method"""
        r = Rectangle(1, 1)
        r.save_to_file([r])
        list_rectangles_output = Rectangle.load_from_file()
        cls.assertEqual([o.to_dictionary()
                        for o in list_rectangles_output], [r.to_dictionary()])

        s = Square(1)
        s.save_to_file([s])
        list_squares_output = Square.load_from_file()
        cls.assertEqual([o.to_dictionary()
                        for o in list_squares_output], [s.to_dictionary()])


if __name__ == "__main__":
    unittest.main()
