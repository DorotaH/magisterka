n, k = map(int, input().split())
ids = list(map(int, input().split()))

k -= 1  # adjust k to 0-based index
i = j = 0

while 1:
    if  i > k:
        print(ids[k])
        break
    if  i == j:
        j = j + 1
    k-=j + 1
    i += 1