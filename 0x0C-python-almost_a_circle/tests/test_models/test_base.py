#!/usr/bin/python3

'''Module for Base unit tests.'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Set up the initial variables before each test method.'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Clean up the variables after each test method.'''
        pass

    def test_base_cls_private_attr(self):
        '''Tests if nb_objects is a private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_base_cls_initialization(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_base_cls_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_base_cls_constructor_without_self_arg(self):
        '''Tests constructor signature without self argument.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        err = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_base_class_constructor_with_2_args_other_than_self(self):
        '''Tests constructor signature with 2 arguments other than self.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        err = "__init__() takes from 1 to 2 positional arguments but" \
              "3 were given"
        self.assertEqual(str(e.exception), err)

    def test_base_class_consecutive_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_base_class_sync_between_class_and_instance_id(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_base_cls_sync_cls_and_inst_id_1_inst(self):
        '''Tests sync between class and instance id with
        more than 1 instance.'''
        b = Base()
        b = Base("Red")
        b = Base(65)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_base_class_custom_id_int(self):
        '''Tests custom int id.'''
        custom_id = 65
        b = Base(custom_id)
        self.assertEqual(b.id, custom_id)

    def test_base_class_custom_id_str(self):
        '''Tests custom string id.'''
        custom_id = "Redman"
        b = Base(custom_id)
        self.assertEqual(b.id, custom_id)

    def test_base_class_id_passed_as_keyword_arg(self):
        '''Tests id passed as keyword arg.'''
        custom_id = 213
        b = Base(id=custom_id)
        self.assertEqual(b.id, custom_id)

    def test_to_json_string_conversion(self):
        """Test the conversion of a list of dictionaries to a JSON string
        using the to_json_string method of the Base class."""

        """Test if to_json_string raises TypeError if called
        without an argument"""
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        error = "to_json_string() missing 1 required" \
                "positional argument: 'list_dictionaries'"
        self.assertEqual(str(e.exception), error)

        """Test if to_json_string returns "[]" when
        called with None or an empty list"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        dictionary = [{'x': 211, 'y': 808080, 'width': 4444777,
                       'id': 324261, 'height': 987232}]
        self.assertEqual(Base.to_json_string(dictionary),
                         '[{"x": 211, "y": 808080, "width": 4444777,'
                         '"id": 324261, "height": 987232}]')

        dictionary = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(Base.to_json_string(dictionary),
                         '[{"x": 1, "y": 2, 
                         "width": 3, "id": 4, "height": 5}]')

        dictionary = [{"bumblebee": 909099}]
        self.assertEqual(Base.to_json_string(dictionary),
                         '[{"bumblebee": 909099}]')

        dictionary = [{"bumblebee": 909099}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(dictionary),
                         '[{"bumblebee": 909099}, {"abc": 123}, {"HI": 0}]')

        dictionary = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
                      {'x': 211, 'y': 808080, 'width': 4444777, 'id': 324261,
                       'height': 987232}]
        self.assertEqual(Base.to_json_string(dictionary),
                         '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, '
                         '{"x": 211, "y": 808080, 
                         "width": 4444777, 
                         "id": 324261,
                         "height": 987232}]')

        dictionary = [{}]
        self.assertEqual(Base.to_json_string(dictionary), '[{}]')

        dictionary = [{}, {}]
        self.assertEqual(Base.to_json_string(dictionary), '[{}, {}]')

        """Test if to_json_string correctly converts objects of Rectangle
        and Square"""
        rect1 = Rectangle(10, 7, 2, 8)
        dictionary = rect1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_result = '[{"id": 1, "x": 2, "y": 8,\
                "width": 10, "height": 7}]'
        self.assertEqual(json_dictionary, expected_result)

        rect2 = Rectangle(2, 5, 1, 6)
        rect3 = Rectangle(4, 8, 7, 2)
        rectangles = [rect1, rect2, rect3]
        rectangle_dicts = [rect.to_dictionary() for rect in rectangles]
        json_rect_dicts = Base.to_json_string(rectangle_dicts)
        self.assertEqual(json.loads(json_rect_dicts), rectangle_dicts)

        s1 = Square(7, 2, 1)
        s2 = Square(3, 4, 5)
        s3 = Square(6, 8, 9)
        squares = [s1, s2, s3]
        square_dicts = [square.to_dictionary() for square in squares]
        json_square_dicts = Base.to_json_string(square_dicts)
        self.assertEqual(json.loads(json_square_dicts), square_dicts)

    def test_save_to_file_method(self):
        '''Tests the save_to_file() method for
        both Rectangle and Square classes.'''

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 100)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 47)

        # Test for Square class
        s1 = Square(10, 7, 2)
        s2 = Square(5)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 81)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        s2 = Square(2)
        Square.save_to_file([s2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 33)

    def test_json_string_conversion(self):
        """Tests the from_json_string() method of Base class."""
        # Tests with no argument and invalid argument
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "from_json_string() missing 1 required" \
            "positional argument: 'json_string'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        # Tests with valid argument
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5},' \
            '{"x": 101, "y": 20123, "width": 312321, "id": 522244,' \
            '"height": 34340}]'
        expected_dict = [{'x': 1, 'y': 2, 'width': 3'id': 4, 'height': 5},
                         {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
                          'height': 34340}]
        self.assertEqual(Base.from_json_string(s), expected_dict)

        expected_dict = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), expected_dict)

        expected_dict = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), expected_dict)

        expected_dict = [{"bumblebee": 909099}, {"abc": 123}, {"HI": 0}]
        s = '[{"bumblebee": 909099}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(s), expected_dict)

        expected_dict = [{"bumblebee": 909099}]
        s = '[{"bumblebee": 909099}]'
        self.assertEqual(Base.from_json_string(s), expected_dict)

        expected_dict = [{'x': 1, 'y': 2, 'width': 3,
                          'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), expected_dict)

        expected_dict = [{'x': 101, 'y': 20123, 'width': 312321,
                          'id': 522244, 'height': 34340}]
        s = '[{"x": 101, "y": 20123, "width": 312321,' \
            '"id": 522244, "height": 34340}]'
        self.assertEqual(Base.from_json_string(s), expected_dict)

        rect_list = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        rect_json = Rectangle.to_json_string(rect_list)
        rect_list_out = Rectangle.from_json_string(rect_json)
        self.assertEqual(rect_list, rect_list_out)

        square_list = [Square(1), Square(2)]
        square_json = Square.to_json_string(square_list)
        square_list_out = Square.from_json_string(square_json)
        self.assertEqual(square_list, square_list_out)

    def test_create_method(self):
        """Tests the create() method of Rectangle class"""

        """Test case 1"""
        rect1 = Rectangle(4, 6, 2, 1, 1)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual(str(rect1), str(rect2))
        self.assertNotEqual(rect1, rect2)
        self.assertIsNot(rect1, rect2)

        """Test case 2"""
        rect1 = Rectangle(1, 1)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual(str(rect1), str(rect2))
        self.assertNotEqual(rect1, rect2)
        self.assertIsNot(rect1, rect2)

        """Test case 3"""
        rect1 = Rectangle(5, 5, 5, 5)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual(str(rect1), str(rect2))
        self.assertNotEqual(rect1, rect2)
        self.assertIsNot(rect1, rect2)

        """Test case 4"""
        rect1 = Rectangle(1, 1, 0, 0, 42)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual(str(rect1), str(rect2))
        self.assertNotEqual(rect1, rect2)
        self.assertIsNot(rect1, rect2)

    def test_load_from_file_method(self):
        """Test the load_from_file() method"""

        rect1 = Rectangle(4, 5, 2, 3, 1)
        rect2 = Rectangle(3, 2, 1, 5, 2)
        list_in = [rect1, rect2]
        file_path = "Rectangle.json"

        """Save the list of objects to a file"""
        Rectangle.save_to_file(list_in)

        """Load the list of objects from the file"""
        list_out = Rectangle.load_from_file()

        """Check if the objects in the list are equal"""
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))

        sqr1 = Square(3, 2, 3, 4)
        sqr2 = Square(5, 4, 3, 2)
        list_in = [sqr1, sqr2]
        file_path = "Square.json"

        """Save the list of objects to a file"""
        Square.save_to_file(list_in)

        """Load the list of objects from the file"""
        list_out = Square.load_from_file()

        # Check if the objects in the list are equal
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))

if __name__ == "__main__":
    unittest.main()
