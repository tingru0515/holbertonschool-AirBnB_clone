#!/usr/bin/python3
"""
This module provides City class inherited from BaseModel
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    This class represents a city.
    """
    state_id = ''
    name = ''
