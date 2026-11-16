def overlapping(list1,list2):  
    d=0
    c = sum(1 for _ in list1)
    for _ in list2:
        d+=1
    for i in range(0,c): 
        for j in range(0,d): 
            if(list1[i]==list2[j]): 
                return 1
    return 0