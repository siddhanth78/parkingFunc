import parkingFunc as pf
import pfTree
import os
import helpmenu

func = None
prevfunc = None

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
            
        if inp == "prevfunc":
            if prevfunc != None:
                func, prevfunc = prevfunc.copy(), func.copy()
            continue
    
        li = inp.split(" ")
        try:
            input_ = [int(i) for i in li]
        except:
            print(">>Invalid function.")
            continue
        else:
            pass
        if func != None:
            prevfunc = func.copy()
        func = pf.getPF(input_)
        if len(func["input"])>10:
            print(">>func[...]")
        else:
            print(f'>>func{func["input"]}')
            
    elif comm == "prevfunc":
        if prevfunc == None:
            print(">>func[]")
            continue
            
        if inp == "":
            if len(prevfunc["input"])>10:
                print(">>func[...]")
            else:
                print(f'>>func{prevfunc["input"]}')
            continue
        else:
            print(">>Function isn't active.")
            continue
        
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
            print("Attributes:")
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
            print(f'    error:        {func["error"]}')
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
            
    elif comm == "tree":
    
        if inp == "":
            print(f'>>Function required.')
            continue
    
        li = inp.split(" ")
        
        if li[0] == 'prevfunc':
            print(">>Function isn't active.")
            continue
        
        if li[0] == 'func':
            if func['isPF'] == False:
                print(">>Invalid function.")
                continue
            if len(li)==1:
                pfTree.getTree(func, processed = False)
                continue
            if li[1] == 'up':
                pfTree.getTree(func, processed = False)
            elif li[1] == 'p':
                pfTree.getTree(func, processed = True)
            else:
                print(">>Invalid input.")
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
        elif inp == "prevfunc":
            helpmenu.prevfunc()
        elif inp == "tree":
            helpmenu.tree()
        elif inp == "quit":
            print("quit")
            print("Quit the terminal.")
        elif inp == "clr":
            print("clr")
            print("Clear the terminal.")
        else:
            print(">>Invalid input.")
            continue
        
        
    else:
        print(">>Invalid input.")
        continue