#!/usr/bin/env python3

"""Define the BaseGeometry class."""


class BaseGeometry():
    """Represent a base geometry class."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise NotImplementedError("area() is not implemented")
