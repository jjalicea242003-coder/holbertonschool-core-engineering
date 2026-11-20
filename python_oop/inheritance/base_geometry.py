#!/usr/bin/env python3

"""Define the BaseGeometry class."""


class BaseGeometry():
    """Represent a base geometry class."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise NotImplementedError("area() is not implemented")
    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value,int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
