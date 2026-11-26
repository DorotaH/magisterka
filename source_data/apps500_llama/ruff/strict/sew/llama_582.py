import sys

mod = 10**9 + 7
n = int(input())

result = 1
for i in range(1, n + 1):
    result = (result * i) % mod

print(result)
