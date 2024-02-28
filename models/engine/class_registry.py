#!/usr/bin/python3
from typing import Type, Optional

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State

CLASS_MAP = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "Place": Place,
    "City": City,
    "Review": Review,
    "State": State
}


def find_class(class_name: str) -> Optional[Type]:
    """
    Find a class in the registry based on the provided class name.

    Parameters:
    - class_name (str): The name of the class to find.

    Returns:
    - class: The class corresponding to the given name,
    or None if not found.
    """
    found_class = CLASS_MAP.get(class_name)
    return found_class
