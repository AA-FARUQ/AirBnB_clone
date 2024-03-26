#!/usr/bin/python3
"""Contains the Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents the Review
    
    Attributes:
    place_id (str): The ID of the place associated with the review.
    user_id (str): The ID of the user who wrote the review.
    review_text (str): The text content of the review.
    """
    
    place_id = ""   # ID of the place associated with the review
    user_id = ""    # ID of the user who wrote the review
    review_text = ""    # Text content of the review
