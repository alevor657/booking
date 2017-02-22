from calendar import monthrange, month_name
from day import Day

class Month():
    def __init__(self, month_number):
        self.month_number = month_number
        self.name = month_name[self.month_number]
        self.days_in_month = []

    def get_nr_of_days(self):
        return monthrange(2017, self.month_number)

    def fill_month(self):
        nr_of_days = self.get_nr_of_days()[1]
        for day in range(nr_of_days):
            d = Day(day + 1)
            self.days_in_month.append(d)

    def get_day(self, day):
        return self.days_in_month[day - 1]

# Testing
m = Month(2)
m.fill_month()
print(m.name)
print(m.get_day(28).number)
