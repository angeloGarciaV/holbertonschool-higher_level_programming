#!/usr/bin/python3
"""Module for square unittests."""
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_base(self):
        """Test the Base class."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def setUp(self):
        """Resets the Base class to 0."""
        Base._Base__nb_objects = 0

    def test_10_squ_inherit(self):
        '''Test if square inherits from Rectangle'''
        self.assertEqual(issubclass(Square, Rectangle), True)


if __name__ == "__main__":
    unittest.main()
