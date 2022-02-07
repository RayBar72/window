#!/usr/bin/python3
"""Unittest eviroment for Rectangle class"""
import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Runs tests for square.py"""

    @classmethod
    def setUpClass(cls):
        """Sets up the testing environment"""

        Base = _Base__nb_objects = 0
        cls.square1 = Square(5)
        cls.square2 = Square(7)
        cls.square3 = Square(2, 2)
        cls.square4 = Square(3, 1, 2)

    def test_201_crea(self):
        """Creation successful"""
        self.assertTrue(self.square1)
        self.assertTrue(self.square2)
        self.assertTrue(self.square3)
        self.assertTrue(self.square4)

    def test_202_sub(self):
        """Squaresubclass of Rectangle and Base"""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_203_check_attrs(self):
        """Attributes of Square setted"""
        self.assertEqual(self.square4.width, 3)
        self.assertEqual(self.square4.height, 3)
        self.assertEqual(self.square4.x, 1)
        self.assertEqual(self.square4.y, 2)

    def test_204_area(self):
        """Calc area"""
        self.assertEqual(self.square1.area(), 25)
        self.assertEqual(self.square2.area(), 49)
        self.assertEqual(self.square3.area(), 4)
        self.assertEqual(self.square4.area(), 9)

    def test_205_display(self):
        """Checking display"""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.square4.display()
        s = f.getvalue()
        self.assertEqual(s, "\n\n ###\n ###\n ###\n")

    def test_206_str(self):
        """Checking __str__ method"""
        self.assertEqual(Square.__str__
                         (self.square1), "[Square] (11) 0/0 - 5")
        self.assertEqual(Square.__str__
                         (self.square2), "[Square] (12) 0/0 - 7")
        self.assertEqual(Square.__str__
                         (self.square3), "[Square] (13) 2/0 - 2")
        self.assertEqual(Square.__str__
                         (self.square4), "[Square] (14) 1/2 - 3")

    def test_207_dict(self):
        """Checking dict"""
        dict1 = self.square1.to_dictionary()
        self.assertDictEqual(dict1, {'size': 5, 'id': 11, 'x': 0, 'y': 0})
        dict2 = self.square2.to_dictionary()
        self.assertDictEqual(dict2, {'size': 7, 'id': 12, 'x': 0, 'y': 0})
        dict3 = self.square3.to_dictionary()
        self.assertDictEqual(dict3, {'size': 2, 'id': 13, 'x': 2, 'y': 0})
        dict4 = self.square4.to_dictionary()
        self.assertDictEqual(dict4, {'size': 3, 'id': 14, 'x': 1, 'y': 2})

    def test_208_x(self):
        """Checking x"""
        self.assertEqual(self.square1.x, 0)
        self.assertEqual(self.square2.x, 0)
        self.assertEqual(self.square3.x, 2)
        self.assertEqual(self.square4.x, 1)

    def test_209_y(self):
        """Checking y"""
        self.assertEqual(self.square1.y, 0)
        self.assertEqual(self.square2.y, 0)
        self.assertEqual(self.square3.y, 0)
        self.assertEqual(self.square4.y, 2)

    def test_210_id(self):
        """Checking id"""
        self.assertEqual(self.square1.id, 11)
        self.assertEqual(self.square2.id, 12)
        self.assertEqual(self.square3.id, 13)
        self.assertEqual(self.square4.id, 14)

    def test_211_x_err(self):
        """Error from x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "ray")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, 2.2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, [2, 1])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "ray")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, (2, 3))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -2)
        with self.assertRaises(TypeError):
            s = Square(1, None)
        with self.assertRaises(TypeError):
            s = Square(1, float('inf'))

    def test_212_y_err(self):
        """Error from y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "ray")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, 2.2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, [2, 1])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "ray")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, (2, 3))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -2)
        with self.assertRaises(TypeError):
            s = Square(1, 1, None)
        with self.assertRaises(TypeError):
            s = Square(1, 1, float('inf'))

    def test_213_size(self):
        """Checking size"""
        s = Square(12)
        self.assertEqual(s.size, 12)
        s.size = 4
        self.assertEqual(s.size, 4)

    def test_214_size_error(self):
        """Error from size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("ray")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(2.2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([2, 1])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square({"ray": 8})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square((3, 2))
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-2)
        with self.assertRaises(TypeError):
            s = Square(None)
        with self.assertRaises(TypeError):
            s = Square(float('inf'))

    def test_215_size(self):
        """Checking size"""
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square2.size, 7)
        self.assertEqual(self.square3.size, 2)
        self.assertEqual(self.square4.size, 3)

    def test_216_update(self):
        """Updating *args"""
        s = Square(4, 3, 1, 98)
        s.update(22, 3, 4, 2)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 22)

    def test_217_update(self):
        """Updating **kwargs"""
        s = Square(4, 3, 1, 98)
        s.update(22, 3, 4, 2, size=15, x=27)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 22)

    def test_218_update(self):
        """Updating **kwargs"""
        s = Square(4, 3, 1, 98)
        s.update(size=15, y=20, x=12, id=8)
        self.assertEqual(s.width, 15)
        self.assertEqual(s.height, 15)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.y, 20)

    def test_219_Dictionary(self):
        """Checking Dictionary"""
        square1_dict = self.square1.to_dictionary()
        self.assertTrue(type(square1_dict), dict)
        s = Square(1)
        self.assertEqual(Square.__str__
                         (s), "[Square] (16) 0/0 - 1")
        s.update(**square1_dict)
        self.assertEqual(Square.__str__
                         (s), "[Square] (11) 0/0 - 5")


if __name__ == '__main__':
    unittest.main()
