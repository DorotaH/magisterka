import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
pairs = [(int(data[i * 2 + 1]), int(data[i * 2 + 2])) for i in range(n)]

results = []

for a, b in pairs:
    count = 0
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
        count += 1
    results.append(count)

for result in results:
    print(result)
