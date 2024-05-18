import os


def editplanets(mainlist):
    os.system('cls')
    if len(mainlist) == 0:
        print("No planets found")
        return

    while True:
        print("Input index planet to edit: ")
        user_input = input()
        try:
            index = int(user_input)
            if index < 0:
                os.system('cls')
                print("Invalid input")
                continue
        except ValueError:
            os.system('cls')
            print("Invalid input")
            continue

        if index > len(mainlist) - 1:
            os.system('cls')
            print("Index out of range")
            continue
        else:
            break

    os.system('cls')

    while True:
        print("Current planet: ")
        print(mainlist[index])
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
            new_name = input()
            if not new_name.strip():
                os.system('cls')
                print("Invalid input")
                continue
            mainlist[index][0] = new_name
            break
        elif choice == "2":
            os.system('cls')
            print("Input new type: ")
            new_type = input()
            if not new_type.strip():
                os.system('cls')
                print("Invalid input")
                continue
            mainlist[index][1] = new_type
            break
        elif choice == "3":
            while True:
                try:
                    os.system('cls')
                    print("Input new mass: ")
                    new_mass = float(input())
                    break
                except ValueError:
                    os.system('cls')
                    print("Invalid input")
                    continue
            mainlist[index][2] = new_mass
            break
        elif choice == "4":
            while True:
                try:
                    os.system('cls')
                    print("Input new temperature: ")
                    new_temp = float(input())
                    break
                except ValueError:
                    os.system('cls')
                    print("Invalid input")
                    continue
            mainlist[index][3] = new_temp
            break
        elif choice == "5":
            while True:
                try:
                    os.system('cls')
                    print("Input new radius: ")
                    new_radius = float(input())
                    break
                except ValueError:
                    os.system('cls')
                    print("Invalid input")
                    continue
            mainlist[index][4] = new_radius
            break
        elif choice == "6":
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Invalid input")
            continue

    os.system('cls')
    print("Edit planet successfully")
