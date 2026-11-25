def is_ladder(arr):
    n = len(arr)
    if n <= 1:
        return True
    i = 1
    while n > i and arr[i] >= arr[i - 1]:
        i += 1
    while n > i and arr[i] <= arr[i - 1]:
        i += 1
    return n == i


n, m = map(int, input().split())
a, queries = (
    list(map(int, input().split())),
    [tuple(map(int, input().split())) for _ in range(m)],
)

results = []
for l, r in queries:
    segment = a[l - 1 : r]
    if not is_ladder(segment):
        results.append("No")
    else:
        results.append("Yes")

for result in results:
    print(result)
