#!/usr/bin/python3
"""Test suite for the State class of the models.state module"""
import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        self.test_state = State()

    def test_state_is_a_subclass_of_basemodel(self):
        """Test if State object is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attr_is_a_class_attribute(self):
        """Test if 'name' is a class attribute"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attributes(self):
        self.assertIs(type(self.test_state.name), str)
        self.assertFalse(bool(self.test_state.name))
