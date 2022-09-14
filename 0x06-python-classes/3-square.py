#!/usr/bin/python3
"""This class Square that defines a square by: (based on 2-square.py)"""

class Square:
    """A class named Square

    Attributes:
    attr(size): size of square
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): The size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Calculates the area based on size of square
        Returns:
        int: The return value. Returns the area
        """
        return self.__size * self.__size
