#!/usr/bin/env python3

"""Define a Square class with size and position."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the aquare."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and update the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Validate and update position."""
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(type(n) is int and n >= 0 for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integer"
                )
            self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters."""
        print(self)

    def __str__(self):
        """Return the square as a string."""
        if self.__size == 0:
            return ""

        row = " " * self.__position[0] + "#" * self.__size
        square = "\n".join([row] * self.__size)

        return "\n" * self.__position[1] + square
