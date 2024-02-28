#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        """Initialize class FileStorage"""

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        self.__objects = value

    @property
    def filepath(self):
        return self.__file_path

    @filepath.setter
    def filepath(self, value):
        self.__file_path = value

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file
        (path: __file_path)."""
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        from .class_registry import find_class
        try:
            with open(self.filepath, 'r') as file:
                obj_dict = json.load(file)
                for value in obj_dict.values():
                    found_class = find_class(value['__class__'])
                    instance = found_class(**value)
                    self.new(instance)
        except (FileNotFoundError):
            pass
