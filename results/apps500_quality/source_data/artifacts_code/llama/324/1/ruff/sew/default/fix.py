import math


def find_composite(a, n):
    """Find the next composite number after a."""
    for  i in  range(1 + a, pow(10, 9)):
        if not is_prime(i):
            return  i


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return  False
    for  i in  range(2, 1 + int(math.sqrt(n))):
        if 0 == n % i:
            return  False
    return True


def solve(n):
    """Find two composite integers a and b such that a - b = n."""
    a = 2
    while True:
        a=find_composite(a, n)
        if  is_prime(a - n):
            b = a - n
            return  f"{a} {b}"

n = int(input())
print(solve(n))
