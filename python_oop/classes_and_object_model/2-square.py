#!/usr/bin/env python3

"""Define a square with size validation."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the square with a validation size."""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
