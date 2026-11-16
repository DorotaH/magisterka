def length_Of_Last_Word(a): 
    l = 0
    x = a.strip() 
    for i in range(len(x)): 
        if not x[i] == " ": 
            l += 1
        else: 
            l = 0
    return l 