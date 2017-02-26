class Team():
    """
    asd
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def get_team_name(self):
        return self.name()
