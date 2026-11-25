import sys

n, k = map(int, input().split())

remainders = set()
for i in range(1, k + 1):
    remainders.add(n % i)

print("Yes" if len(remainders) == k else "No")
