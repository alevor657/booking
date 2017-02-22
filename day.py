class Day():
    def __init__(self, number):
        self.booked = False
        self.number = number
        # self.match = #obj

    def book(self):
        self.booked = True

    def unbook(self):
        self.booked = False

    def is_booked(self):
        return self.booked
