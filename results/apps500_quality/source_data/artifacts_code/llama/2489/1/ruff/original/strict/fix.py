import math

N = int(input())
A = list(map(int, input().split()))

count = 0
primes = []

for i in range(2, int(math.sqrt(max(A)))+1):
    is_prime = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

for i in range(2, max(A)+1):
    is_prime = True
    for p in primes:
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
    else:
        for j in range(len(A)):
            if A[j] != i and i % A[j] == 0:
                break
        else:
            count += 1

print(count)
