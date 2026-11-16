import math 


def find_Digits(n): 
    if (0 > n): 
        return 0;
    if (1 >= n): 
        return 1; 
    x = ((math.log10(n / math.e) * n + math.log10(2 * math.pi * n) / 2.0)); 
    return math.floor(x) + 1;
