#!/usr/bin/python3
"""
This module provides Review class inherited from BaseModel
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    This class represents a review.
    """
    place_id = ''
    user_id = ''
    text = ''
