def count_operations(a, b):
    count = 0
    while a > 0 and 0 < b:
        if a > b:
            a -= b
        else:
            b -= a
        count += 1
    return count


n = int(input())
results = []
for _ in range(n):
    a, b = map(int, input().split())
    results.append(count_operations(a, b))

for result in results:
    print(result)
