#!/usr/bin/python3

'''Module for testing Rectangle class.'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangleClass(unittest.TestCase):

    def setUp(self):
        '''Sets up instances for all test methods'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Cleans up after each test_method'''
        pass

    def test_class_type(self):
        '''Tests if Rectangle is a class'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_inheritance(self):
        '''Tests if Rectangle inherits from Base'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_constructor_no_args(self):
        '''Tests the Rectangle constructor with no arguments'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments:" \
            "'width' and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_constructor_many_args(self):
        '''Tests the Rectangle constructor with too many arguments'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__() takes from 3 to 6 positional arguments but 7 were given"
        self.assertEqual(str(e.exception), s)

    def test_constructor_one_arg(self):
        '''Tests the Rectangle constructor with one argument'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_instantiation_positional(self):
        '''Tests positional instantiation.'''
        r = Rectangle(7, 23, 20, 34)
        d = {'_Rectangle__height': 23, '_Rectangle__width': 7,
             '_Rectangle__x': 20, '_Rectangle__y': 34, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Rectangle(7, 23, 20, 20, 87)
        d = {'_Rectangle__height': 23, '_Rectangle__width': 7,
             '_Rectangle__x': 20, '_Rectangle__y': 34, 'id': 87}
        self.assertEqual(r.__dict__, d)

    def test_instantiation_keyword(self):
        '''Tests positional instantiation.'''
        r = Rectangle(50, 140, id=213, y=71, x=509)
        d = {'_Rectangle__height': 140, '_Rectangle__width': 50,
             '_Rectangle__x': 509, '_Rectangle__y': 71, 'id': 213}
        self.assertEqual(r.__dict__, d)

    def test_id_inherited(self):
        '''Tests if id is inherited from Base.'''
        Base._Base__nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)

    def test_properties(self):
        '''Tests property getters/setters.'''
        r = Rectangle(18, 22)
        r.width = 144
        r.height = 145
        r.x = 146
        r.y = 147
        d = {'_Rectangle__height': 145, '_Rectangle__width': 144,
             '_Rectangle__x': 146, '_Rectangle__y': 147, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 144)
        self.assertEqual(r.height, 145)
        self.assertEqual(r.x, 146)
        self.assertEqual(r.y, 147)

    def test_instantiation(self):
        '''Tests instantiation.'''
        rectangle = Rectangle(10, 20)
        self.assertEqual(str(type(rectangle)),
                         "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(rectangle, Base))
        expected_dict = {
            '_Rectangle__height': 20,
            '_Rectangle__width': 10,
            '_Rectangle__x': 0,
            '_Rectangle__y': 0,
            'id': 1
        }
        self.assertDictEqual(rectangle.__dict__, expected_dict)

        with self.assertRaises(TypeError) as e:
            rectangle = Rectangle("1", 2)
        self.assertEqual(str(e.exception),
                "width must be an integer")

        with self.assertRaises(TypeError) as e:
            rectangle = Rectangle(1, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(TypeError) as e:
            rectangle = Rectangle(1, 2, "3")
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            rectangle = Rectangle(1, 2, 3, "4")
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            rectangle = Rectangle(-1, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            rectangle = Rectangle(1, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            rectangle = Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            rectangle = Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            rectangle = Rectangle(1, 2, -3)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            rectangle = Rectangle(1, 2, 3, -4)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_property(self):
        '''Tests property setting/getting.'''
        r = Rectangle(2, 3)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(20) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_property_range_zero(self):
        '''Tests property setting/getting.'''
        r = Rectangle(2, 3)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def invalid_types(self):
        '''Returns tuple of types for validation.'''
        t = (3.14, -1.1, float('inf'), float('-inf'),
                True, "str", (2,), [4], {5}, {6: 7}, None)
        return t

    def test_00_validate_value_negative_gt(self):
        '''Tests property validation.'''
        r = Rectangle(2, 3)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_01_validate_value_negative_ge(self):
        '''Tests property validation.'''
        r = Rectangle(2, 3)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_validate_value_zero(self):
        '''Tests property validation.'''
        r = Rectangle(2, 3)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_validate_type(self):
        '''Tests property validation.'''
        r = Rectangle(2, 3)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)

    def test_area_no_args(self):
        '''Tests area() method signature.'''
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            r.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_area_computation(self):
        '''Tests area() method computation.'''
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)
        w = randrange(1, 11)
        h = randrange(1, 11)
        r.width = w
        r.height = h
        self.assertEqual(r.area(), w * h)
        w = randrange(1, 11)
        h = randrange(1, 11)
        r = Rectangle(w, h, 7, 8, 9)
        self.assertEqual(r.area(), w * h)
        w = randrange(1, 11)
        h = randrange(1, 11)
        r = Rectangle(w, h, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * h)

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_00_display_no_args(self):
        '''tests display() method signature'''
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            r.display()
        s = "display() missing 1 required " \
            "positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_01_display_output(self):
        '''tests display() method output'''
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(3, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "###\n###\n###\n###\n###\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "       #####\n       " \
            "#####\n       #####\n       " \
            "#####\n       #####\n       #####\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#########\n#########\n#########" \
            "\n#########\n#########\n#########" \
            "\n#########\n#########\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(1, 1, 10, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "          #\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 3, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "     #####\n     #####\n     #####\n"
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 3, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#####\n#####\n#####\n"
        self.assertEqual(f.getvalue(), s)

    def test_str_no_args(self):
        '''Tests __str__() method signature.'''
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            r.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_str(self):
        '''Tests __str__() method return.'''
        r = Rectangle(5, 2)
        s = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(r), s)
        r = Rectangle(1, 1, 1)
        s = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(r), s)
        r = Rectangle(3, 4, 5, 6)
        s = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(r), s)

        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_rectangle_update_with_positional_args(self):
        '''Tests the update() method with positional arguments.'''
        r = Rectangle(5, 2)

        expected_dict = {'_Rectangle__width': 5,
                         '_Rectangle__height': 2,
                         '_Rectangle__x': 0,
                         '_Rectangle__y': 0,
                         'id': 1}
        self.assertEqual(r.__dict__, expected_dict)

        r.update(10)
        expected_dict['id'] = 10
        self.assertEqual(r.__dict__, expected_dict)

        r.update(10, 5)
        expected_dict['_Rectangle__width'] = 5
        self.assertEqual(r.__dict__, expected_dict)

        r.update(10, 5, 17)
        expected_dict['_Rectangle__height'] = 17
        self.assertEqual(r.__dict__, expected_dict)

        r.update(10, 5, 17, 20)
        expected_dict['_Rectangle__x'] = 20
        self.assertEqual(r.__dict__, expected_dict)

        r.update(10, 5, 17, 20, 25)
        expected_dict['_Rectangle__y'] = 25
        self.assertEqual(r.__dict__, expected_dict)

    def test_update_no_args_method_signature(self):
        '''Test update() method signature.'''
        r = Rectangle(5, 2)

        with self.assertRaises(TypeError) as e:
            Rectangle.update()

        self.assertEqual(str(e.exception), "update() missing 1 required "
                                           "positional argument: 'self'")

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_rectangle_update_with_keyword_arguments(self):
        '''Test update() method with keyword arguments.'''
        rect = Rectangle(5, 2)
        d = rect.__dict__.copy()

        rect.update(id=10)
        d["id"] = 10
        self.assertEqual(rect.__dict__, d)

        rect.update(width=5)
        d["_Rectangle__width"] = 5
        self.assertEqual(rect.__dict__, d)

        rect.update(height=17)
        d["_Rectangle__height"] = 17
        self.assertEqual(rect.__dict__, d)

        rect.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rect.__dict__, d)

        rect.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rect.__dict__, d)

    def test_rectangle_update_with_positional_args_bad_val(self):
        '''Tests update() method with positional arguments
        containing bad values.'''
        """Arrange"""
        rect = Rectangle(5, 2)
        d = rect.__dict__.copy()

        rect.update(10)
        d["id"] = 10

        """Assert"""
        self.assertEqual(rect.__dict__, d)

        """Act and Assert"""
        with self.assertRaises(ValueError) as e:
            rect.update(10, -5)
        self.assertEqual(str(e.exception), "width must be > 0")

        """Act and Assert"""
        with self.assertRaises(ValueError) as e:
            rect.update(10, 5, -17)
        self.assertEqual(str(e.exception), "height must be > 0")

        """Act and Assert"""
        with self.assertRaises(ValueError) as e:
            rect.update(10, 5, 17, -20)
        self.assertEqual(str(e.exception), "x must be >= 0")

        """Act and Assert"""
        with self.assertRaises(ValueError) as e:
            rect.update(10, 5, 17, 20, -25)
        self.assertEqual(str(e.exception), "y must be >= 0")

        """Assert"""
        self.assertEqual(rect.__dict__, d)

    def test_rectangle_update_with_keyword_args(self):
        """Test the update() method with keyword arguments."""
        rectangle = Rectangle(5, 2)
        rectangle_dict = rectangle.__dict__.copy()

        rectangle.update(id=10)
        rectangle_dict["id"] = 10
        self.assertEqual(rectangle.__dict__, rectangle_dict)

        rectangle.update(width=5)
        rectangle_dict["_Rectangle__width"] = 5
        self.assertEqual(rectangle.__dict__, rectangle_dict)

        rectangle.update(height=17)
        rectangle_dict["_Rectangle__height"] = 17
        self.assertEqual(rectangle.__dict__, rectangle_dict)

        rectangle.update(x=20)
        rectangle_dict["_Rectangle__x"] = 20
        self.assertEqual(rectangle.__dict__, rectangle_dict)

        rectangle.update(y=25)
        rectangle_dict["_Rectangle__y"] = 25
        self.assertEqual(rectangle.__dict__, rectangle_dict)

    def test_rectangle_update_with_kwargs(self):
        """
        Test update() method with keyword arguments.
        """
        rect = Rectangle(5, 2)
        rect_dict = rect.__dict__.copy()

        rect.update(id=10)
        rect_dict["id"] = 10
        self.assertEqual(rect.__dict__, rect_dict)

        rect.update(id=10, width=5)
        rect_dict["_Rectangle__width"] = 5
        self.assertEqual(rect.__dict__, rect_dict)

        rect.update(id=10, width=5, height=17)
        rect_dict["_Rectangle__height"] = 17
        self.assertEqual(rect.__dict__, rect_dict)

        rect.update(id=10, width=5, height=17, x=20)
        rect_dict["_Rectangle__x"] = 20
        self.assertEqual(rect.__dict__, rect_dict)

        rect.update(id=10, width=5, height=17, x=20, y=25)
        rect_dict["_Rectangle__y"] = 25
        self.assertEqual(rect.__dict__, rect_dict)

        rect.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(rect.__dict__, rect_dict)

        """additional test cases"""
        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1),
                         "[Rectangle] (1) 10/10 - 10/10")

        rect1.update(height=1)
        self.assertEqual(str(rect1),
                         "[Rectangle] (1) 10/10 - 10/1")

        rect1.update(width=1, x=2)
        self.assertEqual(str(rect1),
                         "[Rectangle] (1) 2/10 - 1/1")

        rect1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rect1),
                         "[Rectangle] (89) 3/1 - 2/1")

        rect1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rect1),
                         "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        rect1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect1), "[Rectangle] (1) 10/10 - 10/10")

        rect1.update(89)
        self.assertEqual(str(rect1), "[Rectangle] (89) 10/10 - 10/10")

        rect1.update(89, 2)
        self.assertEqual(str(rect1), "[Rectangle] (89) 10/10 - 2/10")

        rect1.update(89, 2, 3)
        self.assertEqual(str(rect1), "[Rectangle] (89) 10/10 - 2/3")

        rect1.update(89, 2, 3, 4)
        self.assertEqual(str(rect1), "[Rectangle] (89) 4/10 - 2/3")

        rect1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rect1), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_to_dictionary(self):
        '''Tests the to_dictionary() method.'''
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        err = "to_dictionary() missing 1 required" \
              "positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

        r1 = Rectangle(1, 2)
        r1_dict = r1.to_dictionary()
        expected_dict = {'x': 0,
                         'y': 0,
                         'width': 1,
                         'id': 1,
                         'height': 2}
        self.assertEqual(r1_dict, expected_dict)

        r2 = Rectangle(1, 2, 3, 4, 5)
        r2_dict = r2.to_dictionary()
        expected_dict = {'x': 3,
                         'y': 4,
                         'width': 1,
                         'id': 5,
                         'height': 2}
        self.assertEqual(r2_dict, expected_dict)

        r2.x = 10
        r2.y = 20
        r2.width = 30
        r2.height = 40
        expected_dict = {'x': 10,
                         'y': 20,
                         'width': 30,
                         'id': 5,
                         'height': 40}
        self.assertEqual(r2.to_dictionary(), expected_dict)

        r3 = Rectangle(10, 2, 1, 9)
        r3_dict = r3.to_dictionary()
        r4 = Rectangle(1, 1)
        r4.update(**r3_dict)
        self.assertEqual(str(r3), str(r4))
        self.assertNotEqual(r3, r4)

if __name__ == "__main__":
    unittest.main()
