#!/usr/bin/python3
"""Implements the Users model"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user

    Attributes:
        user_email (str): The email of the user.
        user_password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    user_email = ""     # The email of the user
    user_password = ""  # The password of the user
    first_name = ""     # The first name of the user
    last_name = ""      # The last name of the user
