import math


def  gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b:
        a, b=b, a%b
    return  a

n = int(input())
A = [int(x) for x in input().split()]

max_a = max(A)
factors = []
for _ in range(max_a + 1):
    factors.append([])

for i in range(1, int(math.sqrt(max_a)) + 1):
    if  i * i <= max_a:
        factors[i].append(i)
        factors[i*i].append(i)
    if  i <= max_a // i:
        factors[i].append(i*(max_a//i))

for i in range(1, max_a + 1):
    if  len(factors[i]) == 0:
        factors[i].append(i)

count = 0
for i in range(n):
    for factor in factors[A[i]]:
        if factor != A[i]:
            A[i]=False
            break

for i in range(n):
    if  A[i]:
        count = count + 1

print(count)
