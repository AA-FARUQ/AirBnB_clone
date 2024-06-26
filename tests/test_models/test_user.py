#!/usr/bin/python3
"""Test suite for the User class in models.user"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def test_attributes_are_class_attributes(self):
        """Test if 'first_name' and 'last_name' are class attributes"""
        user = User()
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_class_attributes(self):
        """Test types and initial values of class attributes"""
        user = User()
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)
        self.assertTrue(user.first_name == "")
        self.assertTrue(user.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))
