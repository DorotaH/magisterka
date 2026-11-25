n, k = map(int, input().split())
ids = list(map(int, input().split()))

k -= 1  # adjust k to 0-based index
i = 0
j = 0

while True:
    if i > k:
        print(ids[k])
        break
    if i == j:
        j += 1
    k -= 1 + j
    i += 1
