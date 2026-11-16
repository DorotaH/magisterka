def overlapping(list1,list2):  
    c=0
    d=0
    for  i in  list1: 
        c+=1
    for  i in  list2: 
        d+=1
    for  i in  range(c): 
        for j in range(d): 
            if(list1[i]==list2[j]): 
                return 1
    return 0
