def smallest_Divisor(n): 
    if (n % 2 == 0): 
        return 2;
    i = 3;
    while i**2 <= n: 
        if (n % i == 0): 
            return i; 
        i += 2;
    return n; 