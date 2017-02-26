#!/usr/bin/env python3

from handler import Handler

handler = Handler()

# Main menu loop
while True:
    handler.print_menu()
    inp = input(">>> ")

    if "1" in inp:
        handler.list_calendar()

    elif "2" in inp:
        handler.create_team()

    elif "3" in inp:
        handler.list_teams()

    elif "4" in inp:
        handler.create_match()

    elif "5" in inp:
        handler.list_matches()
