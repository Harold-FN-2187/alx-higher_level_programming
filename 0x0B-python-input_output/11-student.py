#!/usr/bin/python3
"""defines a Student class"""


class Student:
    """represents a Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dictionary representation of Student instance
        If attrs is a list of strings,
        only attribute names contained in list must be retrieved
        Otherwise all attributes are retrieved

        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of Student instance
        """

        for i, j in json.items():
            setattr(self, i, j)
