def highest_Power_of_2(n): 
    return next((i for i in range(n, 0, -1) if ((i & (i - 1)) == 0)), 0) 