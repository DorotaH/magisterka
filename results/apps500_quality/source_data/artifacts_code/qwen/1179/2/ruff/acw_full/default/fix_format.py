n, k = map(int, input().split())
ids = list(map(int, input().split()))

# Calculate the position of the k-th identifier to be pronounced
pos = 1
for i in range(n):
    if pos + i * (n - i - 1) >= k:
        pos += (k - 1) // i
        break
    pos += i * (n - i - 1)

print(ids[pos - 1])
