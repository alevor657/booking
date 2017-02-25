from calendar_module import Calendar

class Handler():
    def __init__(self):
        self.calendar = Calendar()

    def print_menu(self):
        menu = """
            ### Menu ###
        1) Print calendar
        2
        3
        """
        print(menu)

    def list_calendar(self):
        print(self.calendar)

        inp = None
        while inp != 0:
            try:
                inp = int(input("Choose month: (0 to exit)\n"))
            except ValueError:
                print("Invalid input")
                continue

            if (inp <= 0 or inp > 12):
                print("Invalid input")
                continue

            self.list_month(inp)
            break



    def list_month(self, month_nr):
        mon = self.calendar.get_month(month_nr)
        print(mon)
        input("Press enter to continue...")
