"""
Calendar module
"""

from month import Month

class Calendar():
    """
    Calendar module. Implements a class for a calender
    """
    def __init__(self, year=2017):
        self.year = year
        self.months = [Month(n, year) for n in range(1, 13)]

    def __str__(self):
        result_string = "Current year is: {year}\n\n".format(year=self.year)
        counter = 1
        for mon in self.months:
            result_string +=    \
            str(counter) +": Month name: {mname}, days: {days}\n"   \
            .format(mname=mon.name, days=mon.get_nr_of_days())

            counter += 1

        return result_string

    def get_month(self, month_nr):
        """
        Returns a month obj by a given number. 1-12
        """
        return self.months[month_nr - 1]

# Testings
# c = Calendar(2017)
# print(c.months[5].get_nr_of_days())
