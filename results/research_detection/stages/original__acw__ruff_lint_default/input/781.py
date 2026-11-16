import math


def count_Divisors(n): 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2): 
        if (n % i == 0): 
            count = count + 1 if ( n // i == i) else count + 2
    return "Even" if (count % 2 == 0) else "Odd" 