from month import Month

class Calendar():
    def __init__(self, year=2017):
        self.year = year
        self.months = [Month(n, year) for n in range(1, 13)]

    def getMonth(self, month_nr):
        return self.months[month_nr - 1]

# Testings
# c = Calendar(2017)
# print(c.months[5].get_nr_of_days())
