#!/usr/bin/python3

"""Unit tests for the Square class"""

import unittest
import io
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests the Square class"""

    def setUp(self):
        """Sets up the testing environment"""
        pass

    def tearDown(self):
        """Cleans up the testing environment"""
        pass

    def test_square_str(self):
        """Tests the __str__ method of the
        Square class"""
        s = Square(2, 2, 2, 2)
        with io.StringIO() as buf, redirect_stdout(buf):
            print(s)
            output = buf.getvalue().strip()
        self.assertEqual(output, "[Square] (2) 2/2 - 2")

    def test_square_to_dictionary(self):
        """Tests the to_dictionary method of the
        Square class"""
        s = Square(2, 2, 2, 2)
        expected = {'id': 2, 'size': 2, 'x': 2, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected)

    def test_square_update(self):
        """Tests the update method of the Square class"""
        s = Square(2, 2, 2, 2)
        s.update(3, 3, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 3/3 - 3")

    def test_square_update_kwargs(self):
        """Tests the update method of the Square class
        with kwargs"""
        s = Square(2, 2, 2, 2)
        s.update(size=3, x=3, y=3, id=3)
        self.assertEqual(str(s), "[Square] (3) 3/3 - 3")

    def test_square_save_to_file(self):
        """Tests the save_to_file method of the
        Square class"""
        s1 = Square(2, 2, 2, 2)
        s2 = Square(3, 3, 3, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            output = f.read()
        expected_output = '[{"id": 2, "size": 2, "x": 2, "y": 2},' \
                          '{"id": 3, "size": 3, "x": 3, "y": 3}]'
        self.assertEqual(output, expected_output)

    def test_square_load_from_file(self):
        """Tests the load_from_file method of the Square class"""
        s1 = Square(2, 2, 2, 2)
        s2 = Square(3, 3, 3, 3)
        Square.save_to_file([s1, s2])
        s_list = Square.load_from_file()
        expected = '[Square] (2) 2/2 - 2\n[Square] (3) 3/3 - 3'
        self.assertEqual(str(s_list[0]) + "\n" + str(s_list[1]), expected)

    def test_square_type(self):
        """Test if Square is an instance of the Square class."""
        self.assertEqual(str(MySquare),
                         "<class 'models.square.MySquare'>")

    def test_inheritance(self):
        """Test if MySquare inherits Base."""
        self.assertTrue(issubclass(MySquare, Base))

    def test_constructor_missing_args(self):
        """Test the Square constructor signature with
        missing arguments."""
        with self.assertRaises(TypeError) as e:
            s = MySquare()
        expected = "__init__() missing 1 required" \
                   "positional argument: 'side'"
        self.assertEqual(str(e.exception), expected)

    def test_constructor_excess_args(self):
        """Test the Square constructor signature with
        excess arguments."""
        with self.assertRaises(TypeError) as e:
            s = MySquare(1, 2, 3, 4, 5)
        expected = "__init__() takes from 2 to 5 positional" \
                   "arguments but 6 were given"
        self.assertEqual(str(e.exception), expected)

    def test_instantiation(self):
        """Test Square instantiation."""
        s = MySquare(10)
        self.assertEqual(str(type(s)), "<class 'models.square.MySquare'>")
        self.assertTrue(isinstance(s, Base))
        expected_dict = {'_Rectangle__height': 10,
                         '_Rectangle__width': 10,
                         '_Rectangle__x': 0,
                         '_Rectangle__y': 0,
                         'id': 1}
        self.assertDictEqual(s.__dict__, expected_dict)

        with self.assertRaises(TypeError) as e:
            s = MySquare("1")
        expected_msg = "side must be an integer"
        self.assertEqual(str(e.exception), expected_msg)

        with self.assertRaises(TypeError) as e:
            s = MySquare(1, "2")
        expected_msg = "x must be an integer"
        self.assertEqual(str(e.exception), expected_msg)

        with self.assertRaises(TypeError) as e:
            s = MySquare(1, 2, "3")
        expected_msg = "y must be an integer"
        self.assertEqual(str(e.exception), expected_msg)

        with self.assertRaises(ValueError) as e:
            s = MySquare(-1)
        expected_msg = "side must be > 0"
        self.assertEqual(str(e.exception), expected_msg)

        with self.assertRaises(ValueError) as e:
            s = MySquare(1, -2)
        expected_msg = "x must be >= 0"
        self.assertEqual(str(e.exception), expected_msg)

        with self.assertRaises(ValueError) as e:
            s = MySquare(1, 2, -3)
        expected_msg = "y must be >= 0"
        self.assertEqual(str(e.exception), expected_msg)

        with self.assertRaises(ValueError) as e:
            s = MySquare(0)
        expected_msg = "side must be > 0"
        self.assertEqual(str(e.exception), expected_msg)

    def test_square_instantiation_with_positional_args(self):
        """Test Square instantiation using positional arguments"""

        square1 = Square(6, 4, 8)
        expected_dict1 = {'_Rectangle__height': 6,
                          '_Rectangle__width': 6,
                          '_Rectangle__x': 4,
                          '_Rectangle__y': 8,
                          'id': 1}
        self.assertEqual(square1.__dict__, expected_dict1)

        square2 = Square(6, 4, 8, 2)
        expected_dict2 = {'_Rectangle__height': 6,
                          '_Rectangle__width': 6,
                          '_Rectangle__x': 4,
                          '_Rectangle__y': 8,
                          'id': 2}
        self.assertEqual(square2.__dict__, expected_dict2)

    def test_square_instantiation_pos_keywords(self):
        """Test Square class instantiation with positional
        and keyword arguments"""
        square = Square(10, x=1, y=2, id=42)
        expected_dict = {'_Rectangle__height': 10,
                         '_Rectangle__width': 10,
                         '_Rectangle__x': 1,
                         '_Rectangle__y': 2,
                         'id': 42}
        self.assertEqual(square.__dict__, expected_dict)

    def test_square_instantiation_inherited_id(self):
        """Test if Square inherits Base's id attribute"""
        Base._Base__nb_objects = 98
        square = Square(2)
        self.assertEqual(square.id, 99)

    def test_square_properties(self):
        """Test Square's properties getters/setters"""
        square = Square(5, 9)
        square.size = 98
        square.x = 102
        square.y = 103
        expected_dict = {'_Rectangle__height': 98,
                         '_Rectangle__width': 98,
                         '_Rectangle__x': 102,
                         '_Rectangle__y': 103,
                         'id': 1}
        self.assertEqual(square.__dict__, expected_dict)
        self.assertEqual(square.size, 98)
        self.assertEqual(square.x, 102)
        self.assertEqual(square.y, 103)

    def test_00_square_area(self):
        """Tests the area() method of the Square class"""
        # Test for missing self argument
        with self.assertRaises(TypeError) as e:
            Square.area()
        error_msg = "area() missing 1 required" \
                    "positional argument: 'self'"
        self.assertEqual(str(e.exception), error_msg)

        # Test area() method computation
        s = Square(6)
        self.assertEqual(s.area(), 36)

        w = randrange(10) + 1
        s.size = w
        self.assertEqual(s.area(), w * w)

        w = randrange(10) + 1
        s = Square(w, 7, 8, 9)
        self.assertEqual(s.area(), w * w)

        w = randrange(10) + 1
        s = Square(w, y=7, x=8, id=9)
        self.assertEqual(s.area(), w * w)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "9"
        self.assertEqual(str(e.exception),
                         "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = 0
        self.assertEqual(str(e.exception),
                         "width must be > 0")

    def invalid_types(self):
        '''Returns tuple of types for validation.'''
        t = (3.14, -1.1, float('inf'),
             float('-inf'), True, "str",(2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_validate_prop_type(self):
        '''Tests validation of property type.'''
        square = Square(1)
        properties = ["x", "y"]
        for prop in properties:
            s = "{} must be an integer".format(prop)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(square, prop, invalid_type)
                self.assertEqual(str(e.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(square, "width", invalid_type)
            self.assertEqual(str(e.exception), s)

    def test_validate_prop_value_neg_gt(self):
        '''Tests validation of property value
        for negative values >.'''
        square = Square(1, 2)
        properties = ["size"]
        for prop in properties:
            s = "width must be > 0".format(prop)
            with self.assertRaises(ValueError) as e:
                setattr(square, prop, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_validate_prop_value_neg_ge(self):
        '''Tests validation of property value
        for negative values >=.'''
        square = Square(1, 2)
        properties = ["x", "y"]
        for prop in properties:
            s = "{} must be >= 0".format(prop)
            with self.assertRaises(ValueError) as e:
                setattr(square, prop, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_validate_prop_value_zero(self):
        '''Tests validation of property value for zero.'''
        square = Square(1, 2)
        properties = ["size"]
        for prop in properties:
            s = "width must be > 0".format(prop)
            with self.assertRaises(ValueError) as e:
                setattr(square, prop, 0)
            self.assertEqual(str(e.exception), s)

    def test_prop_setting_getting(self):
        '''Tests property setting/getting.'''
        square = Square(1, 2)
        properties = ["x", "y", "width", "height"]
        for prop in properties:
            n = randrange(10) + 1
            setattr(square, prop, n)
            self.assertEqual(getattr(square, prop), n)

    def test_prop_range_zero(self):
        '''Tests property range for zero values.'''
        square = Square(1, 2)
        square.x = 0
        square.y = 0
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_string_repr_no_args(self):
        """Test that __str__() raises a TypeError when called
        with no arguments"""
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            str(Square)
        s = "__str__() missing 1 required" \
            "positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_string_repr(self):
        """Test that __str__() returns the
        correct string representation"""
        r = Square(5)
        expected_string = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(r), expected_string)

        r = Square(1, 1)
        expected_string = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(r), expected_string)

        r = Square(3, 4, 5)
        expected_string = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(r), expected_string)

        r = Square(10, 20, 30, 40)
        expected_string = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(r), expected_string)

    def test_display_method_signature(self):
        """Tests the display() method signature."""
        square = Square(9)
        with self.assertRaises(TypeError) as e:
            square.display()
        error_message = "display() missing 1 required" \
                        "positional argument: 'self'"
        self.assertEqual(str(e.exception), error_message)

    def test_display_method_output(self):
        """Tests the display() method output."""
        square1 = Square(1)
        expected_output = "#\n"
        output = get_display_output(square1)
        self.assertEqual(output, expected_output)

        square2 = Square(3)
        expected_output = "###\n###\n###\n"
        output = get_display_output(square2)
        self.assertEqual(output, expected_output)

        square3 = Square(5, 6, 7)
        expected_output = "      #####\n      " \
                          "#####\n      " \
                          "#####\n      " \
                          "#####\n      " \
                          "#####\n"
        output = get_display_output(square3)
        self.assertEqual(output, expected_output)

        square4 = Square(9, 8)
        expected_output = "        #########\n        " \
                          "#########\n        " \
                          "#########\n        " \
                          "#########\n        " \
                          "#########\n        " \
                          "#########\n        " \
                          "#########\n        " \
                          "#########\n        " \
                          "#########\n"
        output = get_display_output(square4)
        self.assertEqual(output, expected_output)

        square5 = Square(1, 1, 10)
        expected_output = " #\n"
        output = get_display_output(square5)
        self.assertEqual(output, expected_output)

        square6 = Square(5)
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        output = get_display_output(square6)
        self.assertEqual(output, expected_output)

        square7 = Square(5, 5)
        expected_output = "     #####\n     " \
                          "#####\n     " \
                          "#####\n     " \
                          "#####\n     " \
                          "#####\n"
        output = get_display_output(square7)
        self.assertEqual(output, expected_output)

        square8 = Square(5, 3)
        expected_output = "   #####\n   " \
                          "#####\n   " \
                          "#####\n   " \
                          "#####\n   " \
                          "#####\n"
        output = get_display_output(square8)
        self.assertEqual(output, expected_output)

        square9 = Square(5, 0, 4)
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        output = get_display_output(square9)
        self.assertEqual(output, expected_output)

        expected_output = "[Square] (1) 0/0 - 5"
        output = str(square1)
        self.assertEqual(output, expected_output)

        expected_output = "[Square] (2) 2/0 - 2"
        output = str(square2)
        self.assertEqual(output, expected_output)

        expected_output = "[Square] (3) 1/3 - 3"
        output = str(square3)
        self.assertEqual(output, expected_output)

    def get_display_output(square):
        """Helper function to get the output of
        the display method."""
        f = io.StringIO()
        with redirect_stdout(f):
            square.display()
        return f.getvalue()

    def test_update_no_args(self):
        """Test that update() raises a TypeError
        if called without arguments"""
        s = Square(5)
        with self.assertRaises(TypeError) as cm:
            s.update()
        self.assertEqual(str(cm.exception),
                         "update() missing 1 required"
                         "positional argument: 'self'")

    def test_update_positional_args(self):
        """Test that update() correctly updates attributes
        with positional arguments"""
        s = Square(5, 2, 3, 4)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")
        s.update(10, 6)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 6")
        s.update(10, 6, 7)
        self.assertEqual(str(s), "[Square] (10) 7/3 - 6")
        s.update(10, 6, 7, 8)
        self.assertEqual(str(s), "[Square] (10) 7/8 - 6")

    def test_update_positional_args_bad(self):
        """Test that update() raises a ValueError when passed
        bad positional arguments"""
        s = Square(5, 2, 3, 4)
        with self.assertRaises(ValueError) as cm:
            s.update(10, -6)
        self.assertEqual(str(cm.exception), "width must be > 0")
        with self.assertRaises(ValueError) as cm:
            s.update(10, 6, -7)
        self.assertEqual(str(cm.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as cm:
            s.update(10, 6, 7, -8)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_update_keyword_args(self):
        """Test that update() correctly updates attributes
        with keyword arguments"""
        s = Square(5, 2, 3, 4)
        s.update(id=10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")
        s.update(size=6)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 6")
        s.update(x=7)
        self.assertEqual(str(s), "[Square] (10) 7/3 - 6")
        s.update(y=8)
        self.assertEqual(str(s), "[Square] (10) 7/8 - 6")

    def test_update_keyword_args_2(self):
        """Test that update() correctly updates attributes with
        mixed positional and keyword arguments"""
        s = Square(5, 2, 3, 4)
        s.update(id=10, size=6)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 6")
        s.update(id=10, size=6, x=7)
        self.assertEqual(str(s), "[Square] (10) 7/3 - 6")
        s.update(id=10, size=6, x=7, y=8)
        self.assertEqual(str(s), "[Square] (10) 7/8 - 6")
        s.update(y=9, id=10, x=11, size=12)
        self.assertEqual(str(s), "[Square] (10) 11/9 - 12")

    def test_square_to_dictionary(self):
        """Test the to_dictionary() method of the Square class"""
        # Test signature
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        expected_msg = "to_dictionary() missing 1 required" \
                       "positional argument: 'self'"
        self.assertEqual(str(e.exception), expected_msg)

        s1 = Square(1)
        s1_dict = {'x': 0, 'y': 0, 'size': 1, 'id': s1.id}
        self.assertEqual(s1.to_dictionary(), s1_dict)

        s2 = Square(9, 2, 3, 4)
        s2_dict = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(s2.to_dictionary(), s2_dict)

        s2.x = 10
        s2.y = 20
        s2.size = 30
        s2_dict = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(s2.to_dictionary(), s2_dict)

        s3 = Square(1, 1)
        s3.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s3))
        self.assertNotEqual(s1, s3)

if __name__ == "__main__":
    unittest.main()
