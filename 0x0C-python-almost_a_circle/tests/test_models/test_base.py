#!/usr/bin/python3

"""Unittest for base module"""

import unittest
from models.base import Base

import sys
sys.path.append('../models')


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def test_creation(self):
        """Test for creating an instance of Base"""
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertIsInstance(b2, Base)
        self.assertEqual(b2.id, 2)

    def test_creation_with_id(self):
        """Test for creating an instance of Base with an id"""
        b1 = Base(10)
        self.assertIsInstance(b1, Base)
        self.assertEqual(b1.id, 10)

        b2 = Base()
        self.assertIsInstance(b2, Base)
        self.assertEqual(b2.id, 310990)
