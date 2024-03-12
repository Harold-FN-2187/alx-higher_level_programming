#!/usr/bin/python3
"""Class Node that defines a node of a singly linked list"""


class Node:
    """Represents a singly linked list node"""
    def __init__(self,data, next_node=None):
        """Initializes a new Node object"""
        self.__data = data
        self.__next_node = next_node

    
    @property
    def data(self):
        """Retrieve private instance attribute data"""
        return (self.__data)
    
    @data.setter
    def data(self, value):
        """Changes the value of __data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
        
    @property
    def next_node(self):
        """Retrieve value of __next_node"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Class that defines a singly linked list """

    def __init__(self):
        """Initialize a new  SinglyLinkedList instance"""
        self.__head = None
    
    def sorted_insert(self, value):
        """Inserts a new Node to  SinglyLinkedList"""

        new 