def getPF(li):
    
    li_copy = li.copy()
    length = len(li_copy)
    
    #Non-decreasing arrangement-------------
    
    li_copy.sort()
    
    #---------------------------------------
    
    num_cars_dict = dict()
    
    flag = 1
    
    pfData = {'isPF':False,
             'input':li,
              'outcome':None,
              'length':length,
             'spec':None,
             'specDetail':None,
             'nonDecArr':li_copy,
             'orderPerm':None,
             'orderPermInv':None,
              'outcomeInv':None,
             'error':None}
    
    if 1 not in li_copy:
        pfData['error'] = "Function doesn't contain preference '1'."
        return pfData
    
    for n in li_copy:
        if n>length:
            pfData['error'] = "Preference can't be greater than length."
            return pfData
        elif n<1:
            pfData['error'] = "Preference can't be zero or lesser."
            return pfData
    
    #Specification----------------------------
    
    for i in range(1, length+1):
        num_cars_dict[i] = li_copy.count(i)
        
    #-----------------------------------------
    
    num_cars_dict_copy = num_cars_dict.copy()
    
    diff = 0
    
    for i in num_cars_dict_copy:
        num_cars_dict_copy[i] = num_cars_dict_copy[i] + diff
        if num_cars_dict_copy[i] >= 1:
            diff = num_cars_dict_copy[i]-1
            num_cars_dict_copy[i] = 1
            
    if diff == 0:
        flag = 1
    else:
        flag = 0
        
    outcome = []
        
    if flag == 1:
        for i in li:
            n=0
            while n==0:
                if i in outcome:
                    i+=1
                else:
                    outcome.append(i)
                    n=1
        pfData['outcome'] = outcome
        pfData['outcomeInv'] = getInverseOP(outcome)
    else:
        pass
            
    if flag == 1:
        orderperm = getOrderPerm(li_copy, li)
        inverseop = getInverseOP(orderperm)
        pfData['isPF'] = True
        pfData['spec'] = list(num_cars_dict.values())
        pfData['specDetail'] = num_cars_dict
        pfData['orderPerm'] = orderperm
        pfData['orderPermInv'] = inverseop
        return pfData
    else:
        pfData['error'] = "One or more cars didn't get a spot."
        return pfData
        
def getOrderPerm(li_copy, li):
    
    li_ = li.copy()
    li_copy_copy = li_copy.copy()
    
    length = len(li_copy_copy)
    
    orderperm = []
    
    map_ = dict()
    
    for i in range(0, length):
        map_[i+1] = li_copy_copy[i]
        
    for j in range(0, length):
        val = checkmap(map_, li_[j])
        orderperm.append(val)
                
    return orderperm

    
def checkmap(map_, val):
    for i in map_:
        if map_[i] == val:
            map_[i] = 0
            return i
            
            
def getInverseOP(orderperm):
    
    orderperm_copy = orderperm.copy()
    length = len(orderperm_copy)
    
    reference = []
    
    inverseOP = []
    
    for i in range(0, length):
        reference.append(i+1)
    
    try:
        for j in reference:
            truepos = orderperm_copy.index(j)
            pos = truepos+1
            inverseOP.append(pos)
    except:
        return None
    else:
        return inverseOP