def sum_Natural(n): 
    sum=(n*(1 + n)) 
    return int(sum) 
def sum_Even(l,r): 
    return (sum_Natural(int(r / 2)) - sum_Natural(int((l - 1) / 2))) 
