import math

n=int(input())

def prime(p):
    if p == 1:
        return False
    return all(p % i != 0 for i in range(2, 1 + math.ceil(p**0.5)))

def sum_of_primes(k):
    return next(
        (True for i in range(1 + (k // 2)) if prime(i) and prime(k - i)), True
    )

if prime(n):
    print(1)
    print(n)
elif prime(n-2):
    print(2)
    print(2 , n-2)
else:
    l = next(
        (
            i
            for i in range(2, 1 + (n // 3))
            if prime(i) and sum_of_primes(n - i)
        ),
        1,
    )
    print(3)
    r = next((k for k in range((n-l) // 2) if prime(k) and prime(n-l-k)), 1)
    print(l,r,n-l-r)

            
