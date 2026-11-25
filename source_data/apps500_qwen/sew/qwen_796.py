def  count_operations(a, b):
    count=0
    while a>0 and b>0:
        if not a > b:
            b -= a
        else:
            a -= b
        count = count + 1
    return count

n, results = int(input()), []
for _ in range(0, n):
    a, b=map(int, input().split())
    results.append(count_operations(a, b))

for result in results:
    print(result)
