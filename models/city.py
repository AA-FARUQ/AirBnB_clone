#!/usr/bin/python3
"""Module containing the City model"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City"""
    state_id = "" # ID of the state associated with the city
    city_name = "" # Name of the city
