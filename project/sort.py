import os


def sort_min_To_max(mainlist,field):
    os.system("cls")
    if len(mainlist) <= 1:
        return mainlist
    else:
        q = mainlist[0]
        L = []
        M = []
        R = []
        for elem in mainlist:
            if elem[field] < q[field]:
                L.append(elem) 
            elif elem[field] > q[field]: 
                R.append(elem) 
            else: 
                M.append(elem)
        return sort_min_To_max(L,field) + M + sort_min_To_max(R,field)
    
def sort_max_To_min(mainlist, field):
    if len(mainlist) <= 1:
        return mainlist
    else:
        q = mainlist[0]
        L = []
        M = []
        R = []
        for elem in mainlist:
            if elem[field] > q[field]:
                L.append(elem) 
            elif elem[field] < q[field]: 
                R.append(elem) 
            else: 
                M.append(elem)
        return sort_max_To_min(L,field) + M + sort_max_To_min(R,field)

def sortplanets(mainlist):  
    while(True):
        os.system('cls')
        OutputOfMenu() 
        try: 
            number = int(input("Enter your choice: "))
        except ValueError:
            os.system('cls')
            OutputOfMenu()
            print("Invalid input")
            continue
        if (number <= 5 and number > 0):
            number-=1
            while(True):

                try:
                    side = int(input("Type in how you want to sort (1 min->max;2 max->min): "))
                except ValueError:
                    os.system('cls')
                    OutputOfMenu()
                    print("Invalid input")
                    os.system("pause")
                    os.system("cls")
                    continue

                if side == 1:
                    sort_list = sort_min_To_max(mainlist, number)
                    mainlist.clear()
                    mainlist.extend(sort_list)
                    os.system("cls")
                    return
                elif side == 2:
                    sort_list = sort_max_To_min(mainlist, number)
                    mainlist.clear()
                    mainlist.extend(sort_list)
                    os.system("cls")
                    return
                else:
                    os.system("cls")
                    OutputOfMenu()
                    print("Incorrect Input")
                    os.system("pause")
        else:
            os.system("cls")
            OutputOfMenu()
            print("Incorrect Input")
            os.system("pause")

            
        
def OutputOfMenu():
    print("""Write number of operation(from 1 to 5): 
Sort by name - 1
Sort by type - 2
Sort by mass - 3
Sort by temperature - 4
Sort by radius - 5""")