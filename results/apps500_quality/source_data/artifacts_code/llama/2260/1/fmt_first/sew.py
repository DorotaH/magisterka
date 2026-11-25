n=int(input())

def power(n):
    if  n<4:
        return  25
    elif  0 == n % 4:
        return power(n//4)%100
    else:
        return (power(n - 1) * 5) % 100


print(power(n))
