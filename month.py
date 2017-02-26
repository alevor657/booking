"""
A month module. Uses default python module 'calendar'
"""

from calendar import monthrange, month_name
from day import Day

class Month():
    """
    Month class
    """
    def __init__(self, month_number, year):
        self.year = year
        self.month_number = month_number
        self.name = month_name[self.month_number]

        self.days_in_month = []
        self.fill_month()

    def __str__(self):
        result_string = "Current month: {month}\n\n"    \
        .format(month=self.name)

        for day in self.days_in_month:
            result_string +=    \
            "{day_nr}. Booked:{booked}\n" \
            .format(day_nr=day.number, booked=day.is_booked())
            if (day.is_booked()):
                result_string += str(day.match)

        return result_string


    def get_nr_of_days(self):
        """
        Returns number of days in a year.

        Works with leap years.
        """
        return monthrange(2017, self.month_number)[1]

    def fill_month(self):
        """
        Fills a month with days instances
        """
        nr_of_days = self.get_nr_of_days()
        for day in range(nr_of_days):
            d = Day(day + 1)
            self.days_in_month.append(d)

    def get_day(self, day):
        """
        Returns a day object by the number. 1-31
        """
        return self.days_in_month[day - 1]

# Testing
# m = Month(2)
# m.fill_month()
# print(m.name)
# print(m.get_day(28).number)
