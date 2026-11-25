n, k = map(int, input().split())
ids = list(map(int, input().split()))

k -= 1  # adjust k to 0-based index
i = 0
j = 0

while True:
    if k < i:
        print(ids[k])
        break
    if i == j:
        j += 1
    k -= j + 1
    i += 1
