#!/usr/bin/env python3

from handler import Handler

handler = Handler()

# Main menu loop
while True:
    handler.printMenu()
    inp = input(">>> ")

    if "1" in inp:
        print(inp)
        # handler.printCalendar()
