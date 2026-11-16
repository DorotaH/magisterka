def check_Odd_Parity(x): 
    parity = 0
    while (x != 0): 
        x = x & (x - 1) 
        parity += 1
    return parity % 2 == 1
