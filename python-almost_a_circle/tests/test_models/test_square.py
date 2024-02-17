#!/usr/bin/python3
"""Module for square unittests."""
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_size(self):
        """Test the size attribute."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s2 = Square(10)
        self.assertEqual(s2.size, 10)

        s3 = Square(7, 0, 0, 12)
        self.assertEqual(s3.size, 7)

        s4 = Square(3, 0, 0, 13)
        self.assertEqual(s4.size, 3)

        s5 = Square(9, 0, 0, 14)
        self.assertEqual(s5.size, 9)

        s6 = Square(1, 0, 0, 15)
        self.assertEqual(s6.size, 1)

        s7 = Square(2, 0, 0, 16)
        self.assertEqual(s7.size, 2)

        s8 = Square(8, 0, 0, 17)
        self.assertEqual(s8.size, 8)

        s9 = Square(6, 0, 0, 18)
        self.assertEqual(s9.size, 6)

        s10 = Square(4, 0, 0, 19)
        self.assertEqual(s10.size, 4)

    def test_size_setter(self):
        """Test the size setter."""
        for value in [5, 10, 7, 3, 9, 1, 2, 8, 6, 4]:
            with self.subTest(value=value):
                s = Square(5)
                s.size = value
                self.assertEqual(s.size, value)

    def test_update(self):
        """Test the update method."""
        s1 = Square(5)
        s1.update(89)
        self.assertEqual(s1.id, 89)

        s2 = Square(10)
        s2.update(89)
        self.assertEqual(s2.id, 89)

        s3 = Square(7, 0, 0, 12)
        s3.update(89)
        self.assertEqual(s3.id, 89)

        s4 = Square(3, 0, 0, 13)
        s4.update(89)
        self.assertEqual(s4.id, 89)

        s5 = Square(9, 0, 0, 14)
        s5.update(89)
        self.assertEqual(s5.id, 89)

        s6 = Square(1, 0, 0, 15)
        s6.update(89)
        self.assertEqual(s6.id, 89)

        s7 = Square(2, 0, 0, 16)
        s7.update(89)
        self.assertEqual(s7.id, 89)

        s8 = Square(8, 0, 0, 17)
        s8.update(89)
        self.assertEqual(s8.id, 89)

        s9 = Square(6, 0, 0, 18)
        s9.update(89)
        self.assertEqual(s9.id, 89)

        s10 = Square(4, 0, 0, 19)
        s10.update(89)
        self.assertEqual(s10.id, 89)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s1 = Square(5)
        self.assertEqual(s1.to_dictionary(), {
            "id": 1,
            "size": 5,
            "x": 0,
            "y": 0
        })

        s2 = Square(10)
        self.assertEqual(s2.to_dictionary(), {
            "id": 2,
            "size": 10,
            "x": 0,
            "y": 0
        })

        s3 = Square(7, 0, 0, 12)
        self.assertEqual(s3.to_dictionary(), {
            "id": 12,
            "size": 7,
            "x": 0,
            "y": 0
        })

        s4 = Square(3, 0, 0, 13)
        self.assertEqual(s4.to_dictionary(), {
            "id": 13,
            "size": 3,
            "x": 0,
            "y": 0
        })

        s5 = Square(9, 0, 0, 14)
        self.assertEqual(s5.to_dictionary(), {
            "id": 14,
            "size": 9,
            "x": 0,
            "y": 0
        })

        s6 = Square(1, 0, 0, 15)
        self.assertEqual(s6.to_dictionary(), {
            "id": 15,
            "size": 1,
            "x": 0,
            "y": 0
        })

        s7 = Square(2, 0, 0, 16)
        self.assertEqual(s7.to_dictionary(), {
            "id": 16,
            "size": 2,
            "x": 0,
            "y": 0
        })

        s8 = Square(8, 0, 0, 17)
        self.assertEqual(s8.to_dictionary(), {
            "id": 17,
            "size": 8,
            "x": 0,
            "y": 0
        })

    def setUp(self):
        """Resets the Base class to 0."""
        Base._Base__nb_objects = 0

    def test_squ_inherit(self):
        '''Test if square inherits from Rectangle'''
        self.assertEqual(issubclass(Square, Rectangle), True)


if __name__ == "__main__":
    unittest.main()
