class Match():
    def __init__(self, sport, teams):
        self.sport = sport
        self.teams = teams

    def __str__(self):
        result = \
        """\
Sport: {sport}
Team1: {t1}
Team2: {t2}
""".format(
        sport=self.sport,
        t1=self.teams[0],
        t2=self.teams[1]
        )

        return result
