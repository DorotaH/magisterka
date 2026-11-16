def count(s,c) : 
    res=0 
    for i in range(len(s)) : 
        if (c == s[i]): 
            res += 1
    return res 
