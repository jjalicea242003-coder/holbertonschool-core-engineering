#!/usr/bin/env python3

"""Define geometric shapes and their properties."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Represent an abstract geometric shape."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize the circle with its radius."""
        self.radius = radius

    def area(self):
        """Calculates the circle area."""
        return self.pi * self.radius ** 2

    def perimeter(self):
        """Calculates the circle perimeter."""
        return 2 * self.pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle dimensions."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the ractangle perimeter."""
        return 2 * (self.witdh + self.height)

def shape_info(Shape):
    """Print the area and the perimeter of a shape."""
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
