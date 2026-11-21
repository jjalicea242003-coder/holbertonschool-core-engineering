#!/usr/bin/env python3

"""Define mixins and a dragon class."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Describe swimming."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Describe flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon."""
    
    def roar(self):
        """Describe the dragon's roar."""
        print("The dragon roars!")
