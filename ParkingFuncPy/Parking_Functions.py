import parkingFunc as pf
import pfTree

func = None

while True:
    user = input(">>")
    
    if ":" in user:
        comm, inp = user.split(":")
    else:
        comm = user
    
    comm = comm.strip()
    inp = inp.strip()
    
    if comm == "input":
        li = inp.split(" ")
        try:
            input_ = [int(i) for i in li]
        except:
            print(">>Invalid function.")
            continue
        else:
            pass
        func = pf.getPF(input_)
        
    elif comm == "func":
        
        if inp == "attr":
            print("Attributes:")
            print(f'    isPF:       {func["isPF"]}')
            print(f'    length:     {func["length"]}')
            print(f'    input:      {func["input"]}')
            print(f'    outcome:    {func["outcome"]}')
            print(f'    outcomeInv: {func["outcomeInv"]}')
            print(f'    nonDecArr:  {func["nonDecArr"]}')
            print(f'    spec:       {func["spec"]}')
            print(f'    specDetail: {func["specDetail"]}')
            print(f'    error:      {func["error"]}')
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
                        print(">>Invalid.")
                        continue
                    else:
                        pass
            else:
                print(">>Invalid input.")
                continue
            
    elif comm == "tree":
        li = inp.split(" ")
        if li[0] == 'func':
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
        
    else:
        print(">>Invalid input.")
        continue