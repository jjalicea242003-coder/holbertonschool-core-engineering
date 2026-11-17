#!/usr/bin/env python3

"""Define a square with controlled acces to its size."""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a square."""
        self.size = size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be >= 0")
        self.__size = value

    def are(self):
        "Represent the area of the square."""
        return self,__size ** 2
