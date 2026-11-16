def find_Min_Sum(num): 
    sum, i = 0, 2
    while(i*i<=num): 
        while(num % i == 0): 
            sum+=i 
            num/=i 
        i += 1
    sum=sum+num 
    return sum
