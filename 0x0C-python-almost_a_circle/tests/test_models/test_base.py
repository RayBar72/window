#!/usr/bin/python3
"""Unittest eviroment for Base Class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Tests for base"""


    @classmethod
    def setUpClass(cls):
        """Set of attributes for class Base"""
        Base.__nb_objects = 0
        cls.base1 = Base()
        cls.base2 = Base()
        cls.base3 = Base(12)
        cls.base4 = Base(1.2)
        cls.base5 = Base("cero")
        cls.rectangle1 = (20, 7, 1, 10)
        cls.rectangle2 = (3, 6)

    def test_001_create(self):
        """Creates Base class"""
        self.assertTrue(self.base1)

    def test_002_create(self):
        """Base with a specified id"""
        self.base1.id = 5
        self.assertEqual(self.base1.id, 5)

    def test_003_id(self):
        """Revising if incrementing right"""
        self.base1.id = 1
        test = self.base1.id
        test2 = self.base2.id
        self.assertEqual(test, test2 - 1)

    def test_004_id(self):
        """Additional incrementing tests"""
        test = self.base1.id
        test2 = self.base2.id
        test3 = self.base3.id
        self.assertEqual(test, test2 - 1)
        self.assertEqual(test3, 22)

    def test_005_id(self):
        """Rev. ids"""
        self.assertTrue(self.base1, 1)
        self.assertTrue(self.base2, 2)
        self.assertTrue(self.base3, 22)
        self.assertTrue(self.base4, 2.2)
        self.assertTrue(self.base5, "two")

    def test_006_Jsonstr(self):
        """Revising the JSON string"""
        dictionary = self.rectangle1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(dictionary), dict)
        self.assertTrue(type(json_dictionary), str)

    def test_007_saveTF(self):
        """Revising file creation and writting"""
        Rectangle.save_to_file([self.rectangle1, self.rectangle2])
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_008_JsonStringFormat(self):
        """Checking JSON string format"""
        list_input = [
            {'id': 100, 'width': 25, 'height': 5},
            {'id': 8, 'width': 11, 'height': 8}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_input), list)
        self.assertTrue(type(json_list_input), str)
        self.assertTrue(type(list_output), list)

    def test_009_create(self):
        """Aditional create tests"""
        rectangle1_dict = self.rectangle1.to_dictionary()
        r = Rectangle.create(**rectangle1_dict)
        self.assertFalse(self.rectangle1 == r)
        self.assertFalse(self.rectangle1 is r)

if __name__ == '__main__':
    unittest.main()
