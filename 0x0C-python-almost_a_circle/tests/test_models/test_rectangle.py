#!/usr/bin/python3
"""Unittest eviroment for Rectangle class"""
import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Class for run tests for Rectangle"""

    @classmethod
    def setUpClass(cls):
        """Set of attributes for class"""

        Base = _Base__nb_objects = 0
        cls.rectangle1 = Rectangle(4, 8)
        cls.rectangle2 = Rectangle(10, 10)
        cls.rectangle3 = Rectangle(3, 4, 2)
        cls.rectangle4 = Rectangle(8, 11, 1, 2, 98)
        cls.rectangle5 = Rectangle(3, 8, 4, 5)

    def test_101_id(self):
        """Revising rectangle id"""
        self.assertEqual(self.rectangle1.id, 6)
        self.assertEqual(self.rectangle2.id, 7)
        self.assertEqual(self.rectangle3.id, 8)
        self.assertEqual(self.rectangle4.id, 98)
        self.assertEqual(self.rectangle5.id, 9)

    def test_102_width(self):
        """Ints added for width"""
        self.assertEqual(self.rectangle1.width, 4)
        self.assertEqual(self.rectangle2.width, 10)
        self.assertEqual(self.rectangle3.width, 3)
        self.assertEqual(self.rectangle4.width, 8)
        self.assertEqual(self.rectangle5.width, 3)

    def test_103_height(self):
        """Ints added for height"""
        self.assertEqual(self.rectangle1.height, 8)
        self.assertEqual(self.rectangle2.height, 10)
        self.assertEqual(self.rectangle3.height, 4)
        self.assertEqual(self.rectangle4.height, 11)
        self.assertEqual(self.rectangle5.height, 8)

    def test_104_x(self):
        """Ints added for x"""
        self.assertEqual(self.rectangle1.x, 0)
        self.assertEqual(self.rectangle2.x, 0)
        self.assertEqual(self.rectangle3.x, 2)
        self.assertEqual(self.rectangle4.x, 1)
        self.assertEqual(self.rectangle5.x, 4)

    def test_105_y(self):
        """Ints added for y"""
        self.assertEqual(self.rectangle1.y, 0)
        self.assertEqual(self.rectangle2.y, 0)
        self.assertEqual(self.rectangle3.y, 0)
        self.assertEqual(self.rectangle4.y, 2)
        self.assertEqual(self.rectangle5.y, 5)

    def test_106_subclass(self):
        """Rectangle subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_107_width_err(self):
        """Errors of width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("ray", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(1.5, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([1, 2], 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({"ray": 5}, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((1, 2), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-2, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(None, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(float('inf'), 1)

    def test_108_height_err(self):
        """Errors of height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "ray")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, 1.5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, [1, 2])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, {"ray": 5})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (1, 2))
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, None)
        with self.assertRaises(TypeError):
            r = Rectangle(1, float('inf'))

    def test_109_x_err(self):
        """Errors for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "ray")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, 1.5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, [1, 2])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, {"ray": 5})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, (1, 2))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, None)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, float('inf'))

    def test_110_y_err(self):
        """Errors for y"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "ray")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, 1.5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, [1, 2])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, {"ray": 5})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, (1, 2))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, None)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, float('inf'))

    def test_111_arg_err(self):
        """Additional args error"""
        with self.assertRaises(TypeError):
            rect_wrong1 = Rectangle(1, 2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect_wrong2 = Rectangle(1)
        with self.assertRaises(TypeError):
            rect_wrong3 = Rectangle()
        with self.assertRaises(TypeError):
            rect_wrong4 = Rectangle(None)

    def test_112_area(self):
        """Revising area"""
        self.assertEqual(self.rectangle1.area(), 32)
        self.assertEqual(self.rectangle2.area(), 100)
        self.assertEqual(self.rectangle3.area(), 12)
        self.assertEqual(self.rectangle4.area(), 88)
        self.assertEqual(self.rectangle5.area(), 24)

    def test_113_area_err(self):
        """Err for area"""
        with self.assertRaises(TypeError):
            self.rectangle1.area(1)
        with self.assertRaises(TypeError):
            self.rectangle1.area("ray")
        with self.assertRaises(TypeError):
            self.rectangle1.area({"ray: 8"})
        with self.assertRaises(TypeError):
            self.rectangle1.area((1, 2))
        with self.assertRaises(TypeError):
            self.rectangle1.area([1, 2])

    def test_114_display(self):
        """Testing display"""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.rectangle1.display()
        s = f.getvalue()
        self.assertEqual(s, "####\n####\n####\n####\n####\n####\n####\n####\n")

    def test_115_display(self):
        """Testing display"""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.rectangle2.display()
        s = f.getvalue()
        self.assertEqual(s, "##########\n##########\n##########\n##########\n##########\n##########\n##########\n##########\n##########\n##########\n")

    def test_116_str(self):
        """Tests __str__"""
        self.assertEqual(Rectangle.__str__
                         (self.rectangle1), "[Rectangle] (6) 0/0 - 4/8")
        self.assertEqual(Rectangle.__str__
                         (self.rectangle2), "[Rectangle] (7) 0/0 - 10/10")
        self.assertEqual(Rectangle.__str__
                         (self.rectangle3), "[Rectangle] (8) 2/0 - 3/4")
        self.assertEqual(Rectangle.__str__
                         (self.rectangle4), "[Rectangle] (98) 1/2 - 8/11")
        self.assertEqual(Rectangle.__str__
                         (self.rectangle5), "[Rectangle] (9) 4/5 - 3/8")

    def test_117_display(self):
        """Testing display"""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.rectangle3.display()
        s = f.getvalue()
        self.assertEqual(s, "  ###\n  ###\n  ###\n  ###\n")

    def test_118_display(self):
        """Testing display"""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.rectangle5.display()
        s = f.getvalue()
        self.assertEqual(s, "\n\n\n\n    ###\n    ###\n    ###\n    ###\n    ###\n    ###\n    ###\n    ###\n")

    def test_119_update_args(self):
        """Testing *args"""
        r = Rectangle(4, 3, 1, 2, 98)
        r.update(22, 3, 4, 2, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 22)

    def test_120_update_kwargs(self):
        """Testing **kwargs"""
        r = Rectangle(4, 3, 1, 2, 98)
        r.update(22, 3, 4, 2, 1, width=1, x=2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 22)

    def test_121_update_width(self):
        """Update non-ints width"""
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, "ray", 1, 1, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1.5, 1, 1, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, {"ray": 8}, 1, 1, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, [1, 2], 1, 1, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, (1, 2), 1, 1, 1)

    def test_122_update_height(self):
        """Update non-ints height"""
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, "ray", 1, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1.5, 1, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, {"ray": 8}, 1, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, [1, 2], 1, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, (1, 2), 1, 1)

    def test_123_update_x(self):
        """Update non-ints x"""
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, "ray", 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, 1.5, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, {"ray": 8}, 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, [1, 2], 1)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, (1, 2), 1)

    def test_124_update_y(self):
        """Update non-ints y"""
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, 1, "ray")
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, 1, 2.2)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, 1, {"ray": 8})
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, 1, [1, 2])
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 1, 1, 1, (1, 2))

    def test_125_update_kwargs_1(self):
        """Testing upd **kwargs"""

        with self.assertRaises(TypeError):
            self.rectangle5.update(1, "hi", 1, 1, 1, width=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, 2.2, 1, 1, 1, x=2)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, {"hi": 2}, 1, 1, 1, height=9)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, [1, 2], 1, 1, 1, y=27)
        with self.assertRaises(TypeError):
            self.rectangle5.update(1, (1, 2), 1, 1, 1, width=12)

    def test_126_update_kwargs_2(self):
        """Testing **kwargs"""
        r = Rectangle(4, 3, 1, 2, 98)
        r.update(x=10, height=30, y=20, width=40, id=8)
        self.assertEqual(r.width, 40)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 20)

    def test_127_update_kwargs_width(self):
        """Update function. **kwargs and width"""
        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(width=20)
        self.assertEqual(r.width, 20)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 20/3")

    def test_128_update_kwargs_height(self):
        """Update function. **kwargs and height"""
        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(height=1)
        self.assertEqual(r.height, 1)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/1")

    def test_129_update_kwargs_x(self):
        """Update function. **kwargs and x"""
        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(x=15)
        self.assertEqual(r.x, 15)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 15/2 - 4/3")

    def test_130_update_kwargs_y(self):
        """Update function. **kwargs and y"""
        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(y=20)
        self.assertEqual(r.y, 20)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/20 - 4/3")

    def test_131_update_kwargs_id(self):
        """Update function. **kwargs and id"""
        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(id=22)
        self.assertEqual(r.id, 22)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (22) 1/2 - 4/3")

    def test_132_update_width(self):
        """Non-ints are passed to width"""
        with self.assertRaises(TypeError):
            self.rectangle5.update(width="ray", height=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(width=1.5, height=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(width={"ray": 8}, height=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(width=[1, 2], height=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(width=(1, 2), height=8, x=5)

    def test_133_update_height(self):
        """Non-ints are passed to height"""
        with self.assertRaises(TypeError):
            self.rectangle5.update(height="ray", width=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(height=1.5, y=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(height={"ray": 8}, width=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(width=5, height=[1, 2], y=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(height=(1, 2), width=8, x=5)

    def test_134_update_x(self):
        """Non-ints are passed to x"""
        with self.assertRaises(TypeError):
            self.rectangle5.update(x="ray", width=8, y=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(x=1.5, y=8, height=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(x={"ray": 8}, width=8, y=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(width=5, x=[1, 2], y=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(x=(1, 2), width=8, y=5)

    def test_135_update_y(self):
        """Non-ints are passed to y"""
        with self.assertRaises(TypeError):
            self.rectangle5.update(y="ray", width=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(y=1.5, x=8, height=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(y={"ray": 8}, width=8, x=5)
        with self.assertRaises(TypeError):
            self.rectangle5.update(width=5, y=[1, 2], x=8)
        with self.assertRaises(TypeError):
            self.rectangle5.update(y=(1, 2), width=8, x=5)

    def test_136_Dictionary(self):
        """Checking to_dictionary"""
        rectangle1_dict = self.rectangle1.to_dictionary()
        self.assertTrue(type(rectangle1_dict), dict)
        r = Rectangle(1, 2)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (10) 0/0 - 1/2")
        r.update(**rectangle1_dict)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (6) 0/0 - 4/8")

    def test_137_Dictionary(self):
        """Direct comparison tests for dictionary"""
        dict1 = self.rectangle1.to_dictionary()
        self.assertDictEqual(dict1, {'width': 4, 'height': 8, 'id': 6,
                                     'x': 0, 'y': 0})
        dict2 = self.rectangle2.to_dictionary()
        self.assertDictEqual(dict2, {'y': 0, 'width': 10, 'x': 0, 'id': 7,
                                     'height': 10})
        dict3 = self.rectangle3.to_dictionary()
        self.assertDictEqual(dict3, {'y': 0, 'width': 4, 'height': 5,
                                     'id': 8, 'x': 1})
        dict4 = self.rectangle4.to_dictionary()
        self.assertDictEqual(dict4, {'x': 1, 'width': 8, 'height': 11,
                                     'id': 98, 'y': 2})
        dict5 = self.rectangle5.to_dictionary()
        self.assertDictEqual(dict5, {'x': 4, 'id': 9, 'y': 5,
                                     'height': 8, 'width': 3})

if __name__ == '__main__':
    unittest.main()
