def isPrime(n): 
    # Corner cases 
    if (1 >= n) : 
        return False
    if (3 >= n) : 
        return True

    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False

    i = 5
    while i**2 <= n: 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = 6 + i

    return True
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    xx = a - b
    yy = a + b
    if xx == 1 and isPrime(yy) == True:
    	print("YES")
    else:
    	print("NO")