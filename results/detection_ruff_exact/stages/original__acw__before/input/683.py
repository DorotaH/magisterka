def sum_Square(n): 
    i = 1
    while i**2 <= n: 
        j = 1
        while j**2 <= n: 
            if i**2 + j**2 == n: 
                return True
            j = j+1
        i = i+1
    return False