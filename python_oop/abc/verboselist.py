#!/usr/bin/env python3

"""Define a list class with operation notifications."""


class VerboseList(list):
    """ """

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list and print a notification."""
        super().extend(items)
        print(f"Extended the lit with [{len(items)}] items.")

    def remove(self, item):
        """Remove an item and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
