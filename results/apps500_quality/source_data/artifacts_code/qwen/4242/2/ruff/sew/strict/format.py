import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
K = int(data[2])


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


divisors = []
for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        divisors.append(i)

divisors.sort(reverse=True)
print(divisors[K - 1])
