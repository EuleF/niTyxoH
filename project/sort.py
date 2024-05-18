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
        q = mainlist[1]
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
    os.system('cls')
    OutputOfMenu()   
    while(True):
        number = int(input())
        if (number <= 5):
            while(True):
                side = int(input("Type in how you want to sort (1 min->max;2 max->min)"))
                if side == 1:
                    sort_list = sort_min_To_max(mainlist, number)
                    mainlist.clear()
                    mainlist.extend(sort_list)
                    break
                elif side == 2:
                    sort_list = sort_max_To_min(mainlist, number)
                    mainlist.clear()
                    mainlist.extend(sort_list)
                    break
                else:
                    os.system("cls")
                    OutputOfMenu()
                    print("Incorrect Input")
                    continue 
            break 
        else:
            os.system("cls")
            OutputOfMenu()
            print("Incorrect Input")
            continue
        
def OutputOfMenu():
    print("""Write number of operation(from 1 to 5): 
Sort by name - 1
Sort by type - 2
Sort by mass - 3
Sort by temperature - 4
Sort by radius - 5""")