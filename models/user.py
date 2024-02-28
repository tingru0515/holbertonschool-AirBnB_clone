#!/usr/bin/python3
"""
This module provides User class inherit from BaseModel
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    This class represents a user.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
