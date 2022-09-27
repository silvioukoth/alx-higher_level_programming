#!/usr/bin/python3
"""Defines the inherited class Mylist."""

class MyList(list):
    """inherits sorted built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
