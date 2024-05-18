import os


def removeplanet(mainlist):
    os.system('cls')
    if len(mainlist) == 0:
        print("No planets found")
        return

    index = 0
    while True:
        print("Input index planet to remove: ")
        try:
            index = int(input())
            if index < 0:
                os.system('cls')
                print("Invalid input")
                continue
        except ValueError:
            os.system('cls')
            print("Invalid input")

        if index > len(mainlist) - 1:
            os.system('cls')
            print("Index out of range")
            continue
        else:
            mainlist.pop(index)
            break
    os.system('cls')
    print("Remove planet successfully")


def clearplanets(mainlist):
    if len(mainlist) == 0:
        print("No planets found")
        os.system('cls')
        return

    mainlist.clear()
    print("Remove planet successfully")
