import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
pairs = []
for i in range(n):
    pairs.append((int(data[2 * i + 1]), int(data[2 * i + 2])))

results = list()

for a, b in pairs:
    count = 0
    while a > 0 and b > 0:
        if not a > b:
            b -= a
        else:
            a -= b
        count += 1
    results.append(count)

for result in results:
    print(result)
