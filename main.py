"""
planets fields
1.name
2.type
3.mass
4.temperature
5.radius
"""
import os
from project import ioput, file, dell, search
mainlist = []


def editplanets():
    pass


def sortpalnets():
    pass


mmenu = {
    0: exit,
    1: ioput.inputplanets,
    2: dell.removeplanet,
    3: dell.clearplanets,
    4: ioput.outputplanets,
    5: ioput.outputtablet,
    6: file.saveplanets,
    7: file.loadpalnets,
    8: search.searchplanets,
    9: editplanets,
    10: sortpalnets
}


def menu():
    while True:
        print("0. Exit\n"
              "1. Add a planet\n"
              "2. Remove a planet\n"
              "3. Remove all planets\n"
              "4. Output planets\n"
              "5. Output planets like a tablet\n"
              "6. Save planets\n"
              "7. Load saved planets\n"
              "8. Search planets\n"
              "9. Edit planets\n"
              "10. Sort planets\n")

        while True:
            try:
                nummenu = int(input("Enter your choice: "))
                if nummenu in mmenu:
                    mmenu[nummenu](mainlist)
                break
            except ValueError:
                print("Invalid input")


os.system('cls')
file.loadpalnets(mainlist)
menu()
