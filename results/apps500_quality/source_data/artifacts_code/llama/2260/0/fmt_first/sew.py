n = int(input())
mod = 100
result = 5
for _ in range(1, n):
    result = (5 * result) % mod
print(result)