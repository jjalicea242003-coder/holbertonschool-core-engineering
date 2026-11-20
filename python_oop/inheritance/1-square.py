#!/usr/bin/env python3

"""This module defines the Square class."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a square with a positive integer size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
