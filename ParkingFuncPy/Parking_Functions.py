import parkingFunc as pf
import pfTree
import os
import helpmenu
from treelib import Tree

func = None
tree = None
pro = False
built = False

print("Parking Functions v3.2")
print("Siddhanth L\n")
print("Type 'help' for more info.\n")

while True:
    user = input(">>")
    
    comm = ""
    inp = ""
    
    if ":" in user:
        comm, inp = user.split(":")
    else:
        comm = user
    
    comm = comm.strip()
    inp = inp.strip()
    
    if comm == "":
        continue
    
    if comm == "clr":
        os.system('cls')
        continue
    
    if comm == "input":
    
        if inp == "":
            continue
    
        li = inp.split(" ")
        try:
            input_ = [int(i) for i in li]
        except:
            print(">>Invalid function.")
            continue
        else:
            pass
        func = pf.getPF(input_)
        if len(func["input"])>10:
            print(">>func[...]")
        else:
            print(f'>>func{func["input"]}')
        
    elif comm == "func":
    
        if func == None:
            print(">>func[]")
            continue
    
        if inp == "":
            if len(func["input"])>10:
                print(">>func[...]")
            else:
                print(f'>>func{func["input"]}')
            continue
        
        if inp == "attr":
            print("\nAttributes:")
            print(f'    isPF:         {func["isPF"]}')
            print(f'    length:       {func["length"]}')
            print(f'    input:        {func["input"]}')
            print(f'    outcome:      {func["outcome"]}')
            print(f'    outcomeInv:   {func["outcomeInv"]}')
            print(f'    nonDecArr:    {func["nonDecArr"]}')
            print(f'    spec:         {func["spec"]}')
            print(f'    specDetail:   {func["specDetail"]}')
            print(f'    orderPerm:    {func["orderPerm"]}')
            print(f'    orderPermInv: {func["orderPermInv"]}')
            print(f'    error:        {func["error"]}\n')
        elif inp == "isPF":
            print(f'>>{func["isPF"]}')
        elif inp == 'input':
            print(f'>>{func["input"]}')
        elif inp == 'outcome':
            print(f'>>{func["outcome"]}')
        elif inp == 'outcomeInv':
            print(f'>>{func["outcomeInv"]}')
        elif inp == 'spec':
            print(f'>>{func["spec"]}')
        elif inp == 'orderPerm':
            print(f'>>{func["orderPerm"]}')
        elif inp == 'orderPermInv':
            print(f'>>{func["orderPermInv"]}')
        elif inp == 'nonDecArr':
            print(f'>>{func["nonDecArr"]}')
        elif inp == 'length':
            print(f'>>{func["length"]}')
        elif inp == 'error':
            print(f'>>{func["error"]}')
        else:
            spd = inp.split(" ")
            if spd[0] == 'specDetail':
                if len(spd) == 1:
                    print(f'>>{func["specDetail"]}')
                elif len(spd) == 2:
                    try:
                        key = int(spd[1])
                    except:
                        print(">>Invalid input.")
                        continue
                    else:   
                        pass
                
                    try:
                        print(f'>>{func["specDetail"][key]}')
                    except:
                        print(">>Invalid position.")
                        continue
                    else:
                        pass
            else:
                print(">>Invalid input.")
                continue
                
    elif comm == "build":
        
        if inp == "":
            continue
            
        if func == None:
            print(">>Invalid input.")
            continue
            
        li = inp.split(" ")
            
        if li[0] == 'func':
            if func['isPF'] == False:
                print(">>Invalid function.")
                continue
            if len(li)==1:
                tree, pro = pfTree.getTree(func, processed = False)
            elif li[1] == 'up':
                tree, pro = pfTree.getTree(func, processed = False)
            elif li[1] == 'p':
                tree, pro = pfTree.getTree(func, processed = True)
                invp, invplen = pfTree.inversionPairs(tree)
            else:
                print(">>Invalid input.")
                continue
            if len(func["input"])>10:
                print(f'>>tree(func[...], {pro})')
            else:
                print(f'>>tree({func["input"]}, {pro})')
        else:
            print(">>Invalid input.")
            continue
            
    elif comm == "tree":
    
        if tree == None:
            print(">>tree[]")
            continue
    
        if inp == "":
            if len(func["input"])>10:
                print(f'>>tree[func[...], {pro}]')
            else:
                print(f'>>tree[{func["input"]}, {pro}]')
        elif inp == 'show':
            if pro == False:
                tree.show()
            elif pro == True:
                tree.show(line_type = 'ascii-em')
        elif inp == 'attr':
            print("\nAttributes:")
            print(f'    func:    {func["input"]}')
            print(f'    pstatus: {pro}')
            if pro == True:
                print(f'    inv:     {invp}\n')
            else:
                print(f'    inv:     None\n')
        elif inp == 'pstatus':
            print(f'>>{pro}')
        elif inp == 'func':
            print("\nInput details:")
            print(f'    func:            {func["input"]}')
            print(f'    func:outcome:    {func["outcome"]}')
            print(f'    func:outcomeInv: {func["outcomeInv"]}\n')
        elif inp == 'inv':
            if pro == True:
                print(f'\nDisplacement of input function: {invplen}')
                print(f'Inversion pairs:                {invp}\n')
            else:
                print(">>Tree must be processed.")
                continue
        else:
            print(">>Invalid input.")
            continue
            
    elif comm == "quit":
        break
        
    elif comm == "help":
        if inp == "":
            helpmenu.help_()
        elif inp == "input":
            helpmenu.input_()
        elif inp == "func":
            helpmenu.func()
        elif inp == "build":
            helpmenu.build()
        elif inp == "tree":
            helpmenu.tree()
        elif inp == "quit":
            print("\nquit")
            print("Quit the terminal.\n")
        elif inp == "clr":
            print("\nclr")
            print("Clear the terminal.\n")
        else:
            print(">>Invalid input.")
            continue
        
        
    else:
        print(">>Invalid input.")
        continue