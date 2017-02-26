"""
A team module
"""

class Team():
    """
    Team class
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def get_team_name(self):
        """
        Returns teams name
        """
        return self.name()
