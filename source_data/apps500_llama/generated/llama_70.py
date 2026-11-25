n = int(input())
mod = 100
result = 5
for _ in range(1, n):
    result = (result * 5) % mod
print(result)
