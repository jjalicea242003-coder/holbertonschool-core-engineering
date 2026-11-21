#!/usr/bin/env python3

"""Define a mudule that """


class Fish:
    """Represent a fish."""

    def swim(self):
        """Describe how the fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Represents the fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Describe how the bird flys."""
        print("The bird is flying")

    def habitat(self):
        """Describe the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flyingfish."""

    def fly(self):
        """Describe how the flying fish flies."""
        print("The flying fish is soaring!")

    def swim(self):
        """Describe swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Represent where the flying fish lives."""
        print("The flying fish lives both in water and the sky!")
