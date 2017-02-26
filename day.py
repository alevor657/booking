"""
Day module
"""

class Day():
    """
    A day class
    """
    def __init__(self, number):
        self.booked = False
        self.number = number
        self.match = None

    def book(self, match):
        """
        Books given day. Needs a match object.
        """
        self.booked = True
        self.match = match

    def unbook(self):
        """
        Unbooks a day
        """
        self.booked = False

    def is_booked(self):
        """
        Returns a bool value
        """
        return self.booked
