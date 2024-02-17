#!/usr/bin/python3
"""Rectangle class unit tests."""
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectnagle(unittest.TestCase):
    """Test cases for the Base class."""

    def test_width(self):
        """Test the width attribute."""
        r1 = Rectangle(5, 2)
        self.assertEqual(r1.width, 5)

        r2 = Rectangle(10, 2)
        self.assertEqual(r2.width, 10)

        r3 = Rectangle(7, 2, 0, 0, 12)
        self.assertEqual(r3.width, 7)

        r4 = Rectangle(3, 2, 0, 0, 13)
        self.assertEqual(r4.width, 3)

        r5 = Rectangle(9, 2, 0, 0, 14)
        self.assertEqual(r5.width, 9)

        r6 = Rectangle(1, 2, 0, 0, 15)
        self.assertEqual(r6.width, 1)

        r7 = Rectangle(2, 2, 0, 0, 16)
        self.assertEqual(r7.width, 2)

        r8 = Rectangle(8, 2, 0, 0, 17)
        self.assertEqual(r8.width, 8)

        r9 = Rectangle(6, 2, 0, 0, 18)
        self.assertEqual(r9.width, 6)

        r10 = Rectangle(4, 2, 0, 0, 19)
        self.assertEqual(r10.width, 4)

    def test_height(self):
        """Test the height attribute."""
        r1 = Rectangle(5, 2)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(10, 2)
        self.assertEqual(r2.height, 2)

        r3 = Rectangle(7, 2, 0, 0, 12)
        self.assertEqual(r3.height, 2)

        r4 = Rectangle(3, 2, 0, 0, 13)
        self.assertEqual(r4.height, 2)

        r5 = Rectangle(9, 2, 0, 0, 14)
        self.assertEqual(r5.height, 2)

        r6 = Rectangle(1, 2, 0, 0, 15)
        self.assertEqual(r6.height, 2)

        r7 = Rectangle(2, 2, 0, 0, 16)
        self.assertEqual(r7.height, 2)

        r8 = Rectangle(8, 2, 0, 0, 17)
        self.assertEqual(r8.height, 2)

        r9 = Rectangle(6, 2, 0, 0, 18)
        self.assertEqual(r9.height, 2)

        r10 = Rectangle(4, 2, 0, 0, 19)
        self.assertEqual(r10.height, 2)

    def test_x(self):
        """Test the x attribute."""
        r1 = Rectangle(5, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(10, 2)
        self.assertEqual(r2.x, 0)

        r3 = Rectangle(7, 2, 0, 0, 12)
        self.assertEqual(r3.x, 0)

        r4 = Rectangle(3, 2, 0, 0, 13)
        self.assertEqual(r4.x, 0)

        r5 = Rectangle(9, 2, 0, 0, 14)
        self.assertEqual(r5.x, 0)

        r6 = Rectangle(1, 2, 0, 0, 15)
        self.assertEqual(r6.x, 0)

        r7 = Rectangle(2, 2, 0, 0, 16)
        self.assertEqual(r7.x, 0)

        r8 = Rectangle(8, 2, 0, 0, 17)
        self.assertEqual(r8.x, 0)

        r9 = Rectangle(6, 2, 0, 0, 18)
        self.assertEqual(r9.x, 0)

        r10 = Rectangle(4, 2, 0, 0, 19)
        self.assertEqual(r10.x, 0)

    def test_y(self):
        """Test the y attribute."""
        r1 = Rectangle(5, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 2)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(7, 2, 0, 0, 12)
        self.assertEqual(r3.y, 0)

        r4 = Rectangle(3, 2, 0, 0, 13)
        self.assertEqual(r4.y, 0)

        r5 = Rectangle(9, 2, 0, 0, 14)
        self.assertEqual(r5.y, 0)

        r6 = Rectangle(1, 2, 0, 0, 15)
        self.assertEqual(r6.y, 0)

        r7 = Rectangle(2, 2, 0, 0, 16)
        self.assertEqual(r7.y, 0)

        r8 = Rectangle(8, 2, 0, 0, 17)
        self.assertEqual(r8.y, 0)

        r9 = Rectangle(6, 2, 0, 0, 18)
        self.assertEqual(r9.y, 0)

        r10 = Rectangle(4, 2, 0, 0, 19)
        self.assertEqual(r10.y, 0)

    def test_area(self):
        """Test the area method."""
        r1 = Rectangle(5, 2)
        self.assertEqual(r1.area(), 10)

        r2 = Rectangle(10, 2)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(7, 2, 0, 0, 12)
        self.assertEqual(r3.area(), 14)

        r4 = Rectangle(3, 2, 0, 0, 13)
        self.assertEqual(r4.area(), 6)

        r5 = Rectangle(9, 2, 0, 0, 14)
        self.assertEqual(r5.area(), 18)

        r6 = Rectangle(1, 2, 0, 0, 15)
        self.assertEqual(r6.area(), 2)

        r7 = Rectangle(2, 2, 0, 0, 16)
        self.assertEqual(r7.area(), 4)

        r8 = Rectangle(8, 2, 0, 0, 17)
        self.assertEqual(r8.area(), 16)

        r9 = Rectangle(6, 2, 0, 0, 18)
        self.assertEqual(r9.area(), 12)

        r10 = Rectangle(4, 2, 0, 0, 19)
        self.assertEqual(r10.area(), 8)

    def test_display(self):
        """Test the display method."""
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.display(), None)

        r2 = Rectangle(3, 2)
        self.assertEqual(r2.display(), None)

        r3 = Rectangle(4, 5, 0, 0, 12)
        self.assertEqual(r3.display(), None)

        r4 = Rectangle(5, 4, 0, 0, 13)
        self.assertEqual(r4.display(), None)

        r5 = Rectangle(6, 7, 0, 0, 14)
        self.assertEqual(r5.display(), None)

        r6 = Rectangle(7, 6, 0, 0, 15)
        self.assertEqual(r6.display(), None)

        r7 = Rectangle(8, 9, 0, 0, 16)
        self.assertEqual(r7.display(), None)

        r8 = Rectangle(9, 8, 0, 0, 17)
        self.assertEqual(r8.display(), None)

        r9 = Rectangle(10, 11, 0, 0, 18)
        self.assertEqual(r9.display(), None)

        r10 = Rectangle(11, 10, 0, 0, 19)
        self.assertEqual(r10.display(), None)

    def test_update(self):
        """Test the update method."""
        r1 = Rectangle(5, 2)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r2 = Rectangle(10, 2)
        r2.update(89)
        self.assertEqual(r2.id, 89)

        r3 = Rectangle(7, 2, 0, 0, 12)
        r3.update(89)
        self.assertEqual(r3.id, 89)

        r4 = Rectangle(3, 2, 0, 0, 13)
        r4.update(89)
        self.assertEqual(r4.id, 89)

        r5 = Rectangle(9, 2, 0, 0, 14)
        r5.update(89)
        self.assertEqual(r5.id, 89)

        r6 = Rectangle(1, 2, 0, 0, 15)
        r6.update(89)
        self.assertEqual(r6.id, 89)

        r7 = Rectangle(2, 2, 0, 0, 16)
        r7.update(89)
        self.assertEqual(r7.id, 89)

        r8 = Rectangle(8, 2, 0, 0, 17)
        r8.update(89)
        self.assertEqual(r8.id, 89)

        r9 = Rectangle(6, 2, 0, 0, 18)
        r9.update(89)
        self.assertEqual(r9.id, 89)

        r10 = Rectangle(4, 2, 0, 0, 19)
        r10.update(89)
        self.assertEqual(r10.id, 89)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r1 = Rectangle(5, 2)
        self.assertEqual(r1.to_dictionary(), {
            "id": 1,
            "width": 5,
            "height": 2,
            "x": 0,
            "y": 0
        })

        r2 = Rectangle(10, 2)
        self.assertEqual(r2.to_dictionary(), {
            "id": 2,
            "width": 10,
            "height": 2,
            "x": 0,
            "y": 0
        })

        r3 = Rectangle(7, 2, 0, 0, 12)
        self.assertEqual(r3.to_dictionary(), {
            "id": 12,
            "width": 7,
            "height": 2,
            "x": 0,
            "y": 0
        })

        r4 = Rectangle(3, 2, 0, 0, 13)
        self.assertEqual(r4.to_dictionary(), {
            "id": 13,
            "width": 3,
            "height": 2,
            "x": 0,
            "y": 0
        })

        r5 = Rectangle(9, 2, 0, 0, 14)
        self.assertEqual(r5.to_dictionary(), {
            "id": 14,
            "width": 9,
            "height": 2,
            "x": 0,
            "y": 0
        })

        r6 = Rectangle(1, 2, 0, 0, 15)
        self.assertEqual(r6.to_dictionary(), {
            "id": 15,
            "width": 1,
            "height": 2,
            "x": 0,
            "y": 0
        })

        r7 = Rectangle(2, 2, 0, 0, 16)
        self.assertEqual(r7.to_dictionary(), {
            "id": 16,
            "width": 2,
            "height": 2,
            "x": 0,
            "y": 0
        })

    def setUp(self):
        """Resets the Base class to 0."""
        Base._Base__nb_objects = 0

    def test_2_rec_inherit(self):
        """Test if rectangle inherits from Base"""
        self.assertEqual(issubclass(Rectangle, Base), True)


if __name__ == "__main__":
    unittest.main()
