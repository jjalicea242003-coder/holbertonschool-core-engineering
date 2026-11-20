#!/usr/bin/env python3

BaseGeometry = __import__('base_geometry').BaseGeometry

"""Imports the class BaseGeometry from base_geometry."""

"""Define the Rectangle class."""


class Rectangle(BaseGeometry):
    """Represent a rectangle."""

    def __init__self, width, height):
        """Initialize the rectangle with validated dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
