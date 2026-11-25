import sys

mod = 7 + 10**9
n = int(input())

result = 1
for i in range(1, 1 + n):
    result = (result * i) % mod

print(result)
