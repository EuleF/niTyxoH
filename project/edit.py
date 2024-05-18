import os


def editplanets(mainlist):
    os.system('cls')
    if len(mainlist) == 0:
        print("No planets found")
        return

    index = 0
    while True:
        print("Input index planet to edit: ")
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
            break

    os.system('cls')
    print("Current planet: ")
    print(mainlist[index])
    while True:
        os.system('cls')
        print("1. Edit name")
        print("2. Edit type")
        print("3. Edit mass")
        print("4. Edit temperature")
        print("5. Edit radius")
        print("6. Back")
        choice = input()

        if choice == "1":
            os.system('cls')
            print("Input new name: ")
            mainlist[index][0] = input()
            break
        elif choice == "2":
            os.system('cls')
            print("Input new type: ")
            mainlist[index][1] = input()
            break
        elif choice == "3":
            while True:
                try:
                    os.system('cls')
                    print("Input new mass: ")
                    mainlist[index][2] = float(input())
                    break
                except ValueError:
                    os.system('cls')
                    print("Invalid input")
                    continue
            break
        elif choice == "4":
            while True:
                try:
                    os.system('cls')
                    print("Input new temperature: ")
                    mainlist[index][3] = float(input())
                    break
                except ValueError:
                    os.system('cls')
                    print("Invalid input")
                    continue
            break
        elif choice == "5":
            while True:
                try:
                    os.system('cls')
                    print("Input new radius: ")
                    mainlist[index][4] = float(input())
                    break
                except ValueError:
                    os.system('cls')
                    print("Invalid input")
                    continue
            break
        elif choice == "6":
            return
        else:
            os.system('cls')
            print("Invalid input")
            continue

    os.system('cls')
    print("Edit planet successfully")
