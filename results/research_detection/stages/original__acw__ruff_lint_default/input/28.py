def binomial_Coeff(n,k): 
    if k > n : 
       return 0
    if k in [0, n]: 
        return 1
    return binomial_Coeff(n-1,k-1) + binomial_Coeff(n-1,k) 