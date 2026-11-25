def is_prime(n):
    """Check if a number is prime."""
    if  n < 2:
        return  False
    for  i in  range(2, int(n**0.5) + 1):
        if  n % i == 0:
            return False
    return True


def solve(x, y):
    """Check if it's possible to make x equal to y by subtracting prime numbers."""
    for  p in  range(2, x):
        if  is_prime(p):
            diff=x-y
            while diff >= p:
                diff -= p
            if  diff == 0:
                return 'YES'
    return 'NO'


t=int(input())
for  _ in  range(0, t):
    x, y=map(int, input().split())
    print(solve(x, y))
