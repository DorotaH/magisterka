n, k = map(int, input().split())
ids = list(map(int, input().split()))

# Calculate the position of the k-th identifier to be pronounced
pos = 1
for i in range(n):
    if pos + (n - i - 1) * i >= k:
        pos += (k - 1) // i
        break
    pos += (n - i - 1) * i

print(ids[pos - 1])
