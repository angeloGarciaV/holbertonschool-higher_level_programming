#!/usr/bin/python3
"""Rectangle class unit tests."""
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectnagle(unittest.TestCase):
    """Test cases for the Base class."""

    def test_rectangle(self):
        """Test the Base class."""
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 4)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 7, 2, 8, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r4.id, 3)

        r5 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r5.id, 4)

        r6 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r6.id, 5)

        r7 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r7.id, 6)

        r8 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r8.id, 7)

        r9 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r9.id, 8)

        r10 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r10.id, 9)

        r11 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r11.id, 10)

        r12 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r12.id, 11)

        r13 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r13.id, 12)

        r14 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r14.id, 13)

        r15 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r15.id, 14)

        r16 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r16.id, 15)

        r17 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r17.id, 16)

        r18 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r18.id, 17)

    def setUp(self):
        """Resets the Base class to 0."""
        Base._Base__nb_objects = 0

    def test_2_rec_inherit(self):
        """Test if rectangle inherits from Base"""
        self.assertEqual(issubclass(Rectangle, Base), True)


if __name__ == "__main__":
    unittest.main()
