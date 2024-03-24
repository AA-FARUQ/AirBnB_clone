#!/usr/bin/python3
"""Test suite for Amenity class of the models.amenity module"""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up test fixtures, instantiate Amenity object"""
        self.test_amenity = Amenity()

    def test_amenity_is_a_subclass_of_basemodel(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.test_amenity), BaseModel))

    def test_name_attribute_is_a_class_attribute(self):
        """Test if 'name' is a class attribute of Amenity"""
        self.assertTrue(hasattr(self.test_amenity, "name"))

    def test_class_attribute_type(self):
        """Test the type of the 'name' attribute"""
        self.assertIs(type(self.test_amenity.name), str)
        self.assertFalse(bool(getattr(self.test_amenity, "name")))
