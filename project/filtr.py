from project import ioput


def filtrationplanets(mainList):
    cls()
    OutputOfMenu()
    numberOfOperation = "";
    element = ""
    
    while(True):
        numberOfOperation = input()
        cls()
        
        if(numberOfOperation == "1"):
            print("Write the name of the element")
            element = input()
            
        elif(numberOfOperation == "2"):
            print("Write the type of the element")
            element = input()
            
        elif(numberOfOperation == "3"):
            print("Write the mass of the element")
            while(True):
                element = input()
                if(element.isdigit()):
                    element = int(element)
                    break;
                else:
                    cls()
                    print("Incorrect input! Write the mass of the element")
                    continue
                
        elif(numberOfOperation == "4"):
            print("Write the temperature of the element")
            while(True):
                element = input()
                if(element.isdigit()):
                    element = int(element)
                    break;
                else:
                    cls()
                    print("Incorrect input! Write the temperature of the element")
                    continue
            
        elif(numberOfOperation == "5"):
            print("Write the radius of the element")
            while(True):
                element = input()
                if(element.isdigit()):
                    element = int(element)
                    break;
                else:
                    cls()
                    print("Incorrect input! Write the radius of the element")
                    continue
            
        else:
            cls()
            OutputOfMenu()
            print("Incorrect Input")
            continue
        cls()
        break;
    numberOfOperation = int(numberOfOperation)-1
    search(numberOfOperation, element, mainList);


def search(numberOfOperation, element, mainList):
    temp = []
    counter = 0
    for mainEl in mainList:
        if(str(element) != "" and str(element) in str(mainEl[numberOfOperation])):
            temp.append(mainEl)
            counter += 1
    if(counter == 0):
        print("MainList doesn't consist ", element, "C:")
    else:
        ioput.outputtablet(temp)


def OutputOfMenu():
    print("""Write number of operation(from 1 to 5): 
Filtration for the elements using the name - 1
Filtration for the elements using the type - 2
Filtration for the elements using the mass - 3
Filtration for the elements using the temperature - 4
Filtration for the elements using the radius - 5""")


def cls():
    print("\033[H\033[J", end="")
