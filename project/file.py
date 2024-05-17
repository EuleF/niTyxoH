def saveplanets(mainlist):
    file = open('save.txt', 'w')
    for planets in mainlist:
        file.write(planets[0] + '\n')
        file.write(planets[1] + '\n')
        file.write(str(planets[2]) + '\n')
        file.write(str(planets[3]) + '\n')
        file.write(str(planets[4]) + '\n')
    file.close()
    print('Saved successfully')


def loadpalnets(mainlist):
    counter = 0
    i = 0
    mainlist.clear()
    mainlist.append([])
    file = open('save.txt', 'r')

    for line in file:
        if counter == 5:
            mainlist.append([])
            i += 1
            counter = 0
        mainlist[i].append(line.rstrip('\n'))
        counter += 1
    file.close()
    print("Data loaded")