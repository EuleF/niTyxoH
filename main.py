"""
planets fields
1.name
2.type
3.mass
4.temperature
5.radius
"""
mainlist = [[]]


def inputplanets():
    print(1)


def remuveplanet():
    pass


def clearplanets():
    pass


def outputplanets():
    pass


def outputtablet():
    pass


def saveplanets():
    pass


def loadpalnets():
    pass


def searchplanets():
    pass


def editplanets():
    pass


def sortpalnets():
    pass


mmenu = {
    0: exit,
    1: inputplanets,
    2: remuveplanet,
    3: clearplanets,
    4: outputplanets,
    5: outputtablet,
    6: saveplanets,
    7: loadpalnets,
    8: searchplanets,
    9: editplanets,
    10: sortpalnets
}


def menu():
    nummenu = -1
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
                return mmenu[nummenu]()
            break
        except ValueError:
            print("Invalid input")
            continue


menu()

# mainlist[0].append(1)
# mainlist[0].append(2)
# mainlist[0].append(3)
# mainlist[0].append(4)
# mainlist[0].append(5)
# mainlist.append([])
# mainlist[1].append(1)
# mainlist[1].append(2)
# mainlist[1].append(3)
# mainlist[1].append(4)
# mainlist[1].append(5)
# print(mainlist)
