#!/usr/bin/python3
"""Contains the State model"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a State

    Attributes:
        state_name (str): The name of the state.
    """

    state_name = "" # The name of the state
