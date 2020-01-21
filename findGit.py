#!/usr/bin/env python3

# This program searches for a keyword in the title on a GitHub page.
# Make a file (.txt) containing multiple GitHub URLs one below the other,
# like this:
#
# GitHub_URL1
# GitHub_URL2
# GitHub_URL3
#
# Enter the word you are looking for, and
# Provide full file path with GitHub_URLs
#
# The program will search a matching of the word in the page title (title tag).
#
# by Diego Moicano (@hihackthis)
# January 07th, 2020
#
# Run: python3 findGit.py
#

import re
import requests
import time
from lxml import html
from colorama import Fore, Back, Style, init

# Start color module
init()


# Start of search function, file entry with URLs.
def search():
    """ Search in the list """
    file_path = input("Enter file path: ")

    # Start of search loop and input of the word to be searched.
    cond = "Y"
    while cond == "Y":
        key_word = input("Enter only one word to search: ")
        ver_word = key_word.split()
        print()

        # The word is separated, if it has more than one, it does not go through the condition.
        # Then the file is opened, each site is separated, then accessed, the words of the title tag are separated,
        # then sorted, to be compared with the searched word, all in small letter.
        if len(ver_word) != 0 and len(ver_word) == 1:
            with open(file_path, "r") as inline:
                read_file = inline.read()
                line = read_file.split("\n")
                for url in line:
                    site = requests.get(url)
                    trees = html.fromstring(site.content)
                    title = trees.xpath(".//title")[0].text
                    words_title = title.split()
                    low = [element.lower() for element in words_title]
                    order = (sorted(low))
                    if key_word.lower() in order:
                        try:
                            print()
                            print(re.sub("(GitHub -)((.*):)?", "",
                                         (Back.RED + Style.BRIGHT + "Title:{}".format(title) + Style.RESET_ALL))
                                  )
                            print(Style.BRIGHT + "URL:  {}".format(url))
                            print(
                                Fore.GREEN + Style.BRIGHT + "OnLine" + Style.RESET_ALL
                                if site.status_code == requests.codes.ok else
                                Fore.RED + Style.BRIGHT + "OffLine" + Style.RESET_ALL
                            )
                            print(Style.RESET_ALL)
                        except ValueError:
                            pass
                    elif key_word.lower() not in low:
                        pass
                    time.sleep(1)
        elif len(ver_word) == 0 or len(ver_word) > 1:
            print()
            print(Fore.RED + Style.BRIGHT + "Please, enter only one word!" + Style.RESET_ALL)
            print()

        # Ask if you want to search again or quit the program.
        cond = input("New search? [Y/N] ").upper()
        print()
        if cond == "Y":
            continue
        elif cond != "Y":
            print("Bye bye! :-D")
            exit()


# The main menu function displays the program banner, searches or exits, and besides,
# checks if typed a number valid or belonging menu number.
def menu():
    """ Start main menu """

    print()
    print(Fore.MAGENTA + Style.BRIGHT + "################################" + Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + r"  __ _           _ _____ _ _   ")
    print(r" / _(_)         | |  __ (_) |  ")
    print(r"| |_ _ _ __   __| | |  \/_| |_ ")
    print(r"|  _| | '_ \ / _` | | __| | __|")
    print(r"| | | | | | | (_| | |_\ \ | |_ ")
    print(r"|_| |_|_| |_|\__,_|\____/_|\__|" + Style.RESET_ALL)
    print()
    print(Fore.CYAN + Style.BRIGHT + "-by Diego Moicano *@hihacktis -- " + Style.RESET_ALL)
    print()
    print(Fore.MAGENTA + Style.BRIGHT + "################################" + Style.RESET_ALL)
    print(Style.RESET_ALL)

    op = True
    while op:
        print("""
              1.Search
              2.Exit or press ENTER
           """)

        op = input("Choose an option: ")
        print()

        try:
            if len(op) == 0 or int(op) == 2:
                print("Bye bye! :-D")
                exit()
            elif int(op) == 1:
                search()
            elif int(op) >= 3 or int(op) < 0:
                print()
                print(
                    Fore.YELLOW + Style.BRIGHT + ">>>> " + Style.RESET_ALL + Fore.RED
                    + Style.BRIGHT + "Please enter a menu number: " + Style.RESET_ALL
                )
        except ValueError:
            print()
            print(
                Fore.YELLOW + Style.BRIGHT + ">>>> " + Style.RESET_ALL + Fore.RED
                + Style.BRIGHT + "Please enter a valid number: " + Style.RESET_ALL
            )


# Calls the main menu
menu()
