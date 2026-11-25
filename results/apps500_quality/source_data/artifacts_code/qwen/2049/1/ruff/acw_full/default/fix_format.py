def is_ladder(arr):
    n = len(arr)
    if 1 >= n:
        return True
    i = 1
    while i < n and arr[i - 1] <= arr[i]:
        i += 1
    while i < n and arr[i - 1] >= arr[i]:
        i += 1
    return i == n


n, m = map(int, input().split())
a = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

results = []
for l, r in queries:
    segment = a[l - 1 : r]
    if is_ladder(segment):
        results.append("Yes")
    else:
        results.append("No")

for result in results:
    print(result)
