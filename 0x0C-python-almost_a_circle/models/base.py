#!/usr/bin/python3
"""Base model"""
import json


class Base:
    """
    Base class
    Attributes:
        __nb_objects (int)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation method
        Args:
            id (int): integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converting a obj to json string
        Args:
            list_dictionaries(list) : list of dictionaries
        Return:
            []: if list_dictionaries is none or empty
            json string representation
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a json string representation to a file
        Args:
            list_objs (list)
        """
        list_of_dict = []
        json_string = "[]"
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                list_of_dict.append(obj.to_dictionary())

            if list_of_dict:
                json_string = Base.to_json_string(list_of_dict)
        with open(filename, 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        converting a json string to a obj
        Args:
            json_string(str): string representing a list of dictionaries
        Return:
            list of json string reprsentation
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instace of all attributes
        Args:
            **dictionary : a double pointer to a dictionary
        """
        dummy = None
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        reads file content and returns a list of instances
        Return:
            List
        """
        filename = cls.__name__ + '.json'
        instances = []
        try:
            with open(filename, encoding='utf-8') as f:
                list_of_dicts = cls.from_json_string(f.read())
                for item in list_of_dicts:
                    instances.append(cls.create(**item))
        except Exception:
            pass
        return instances
