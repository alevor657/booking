#!/usr/bin/env python3

from handler import Handler

handler = Handler()

# Main menu loop
while True:
    handler.print_menu()
    inp = input(">>> ")

    if "1" in inp:
        handler.list_calendar()
