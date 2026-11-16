def cube_Sum(n): 
    sum=0   
    for i in range(n) : 
        sum = sum + (2*i+1)*(2*i+1)*(2*i+1) 
    return sum