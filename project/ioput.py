import os
from prettytable import PrettyTable


def inputplanets(mainlist):
    while True:
        os.system('cls')
        print("Input name planets: ")
        name = input()
        if name != '':
            break

    while True:
        os.system('cls')
        print("Input type planets: ")
        typep = input()
        if typep != '':
            break

    os.system('cls')
    while True:
        try:
            print("Input mass of planets: ")
            mass = float(input())
            break
        except ValueError:
            os.system('cls')
            print("Invalid input")

    os.system('cls')
    while True:
        try:
            print("Input temperature of planets: ")
            temperature = float(input())
            os.system('cls')
            break
        except ValueError:
            os.system('cls')
            print("Invalid input")

    os.system('cls')
    while True:
        try:
            print("Input radius of planets: ")
            radius = float(input())
            break
        except ValueError:
            os.system('cls')
            print("Invalid input")

    os.system('cls')
    mainlist.append([name, typep, mass, temperature, radius])


def outputplanets(mainlist):
    if len(mainlist) == 0:
        os.system('cls')
        print("No planets found")
        return

    os.system('cls')
    for planets in mainlist:
        print(f" Name: {planets[0]}")
        print(f" Type: {planets[1]}")
        print(f" Mass: {planets[2]}")
        print(f" Temperature: {planets[3]}")
        print(f" Radius: {planets[4]}")
        print("")
    os.system('pause')
    os.system('cls')


def outputtablet(mainlist):
    index = 0
    if len(mainlist) == 0:
        os.system('cls')
        print("No planets found")
        return
    os.system('cls')
    table = PrettyTable(['Id', 'Name', 'Type', 'Mass', 'Temperature', 'Radius'])
    for planets in mainlist:
        table.add_row([index, planets[0], planets[1], planets[2], planets[3], planets[4]])
        index += 1
    print(table)
    os.system('pause')
    os.system('cls')
