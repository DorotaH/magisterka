def even_or_odd(N): 
    l = len(N)
    if N[l - 1] in ['0', '2', '4', '6', '8', 'A', 'C', 'E']: 
        return ("Even")
    else: 
        return ("Odd")
