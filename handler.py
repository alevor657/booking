from calendar_module import Calendar
from team import Team
from match import Match

class Handler():
    def __init__(self):
        self.all_matches = []
        self.all_teams = []
        self.calendar = Calendar()

    def print_menu(self):
        menu = """
            ### Menu ###
        1) Print calendar
        ##################
        2) Create team
        3) List all created teams
        4) Create match
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

    def create_team(self):
        t = Team(input("Team name:\n"))
        self.all_teams.append(t)
        print(t, "created")

    def create_match(self):
        sport = input("Type of sport:\n")
        self.list_teams()
        team1 = self.all_teams[int(input("Choose team 1:\n")) - 1]
        team2 = self.all_teams[int(input("Choose team 2:\n")) - 1]

        mo = int(input("Choose month (1-12):\n"))
        month = self.calendar.get_month(mo)

        da = int(input("Choose day (1-" + str(month.get_nr_of_days()) + "):\n"))
        day = month.get_day(da)

        if (day.is_booked()):
            print("The day is already booked for a match!")
            return

        m = Match(sport, (team1, team2))
        day.book(m)

        self.all_matches.append(m)

        print(
        "Match booked month:{m}/day:{d}"    \
        .format(m=mo, d=da)
        )
        self.list_matches()

    def list_matches(self):
        counter = 1
        for m in self.all_matches:
            print("{count}:\n {match}\n\n".format(
            count=counter, match=m
            ))
            counter += 1
        input("Press anykey to continue...")


    def list_teams(self):
        result = "All teams:\n\n"
        counter = 1

        for t in self.all_teams:
            print(str(counter) + ": " + str(t))
            counter += 1
        input("Press enter to continue...")
