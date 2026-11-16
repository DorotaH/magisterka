def largest_pos(list1): 
    max = list1[0] 
    for x in list1: 
        if max < x : 
             max = x  
    return max
