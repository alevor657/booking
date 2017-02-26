class Day():
    def __init__(self, number):
        self.booked = False
        self.number = number
        self.match = None

    def book(self, match):
        self.booked = True
        self.match = match

    def unbook(self):
        self.booked = False

    def is_booked(self):
        return self.booked
