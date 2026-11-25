import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

results = []

for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    l1 = int(data[index + 2])
    r1 = int(data[index + 3])
    l2 = int(data[index + 4])
    r2 = int(data[index + 5])
    index += 6

    total_length = (r1 - l1 + 1) * (r2 - l2 + 1)
    current_intersection = min(r1, r2) - max(l1, l2) + 1
    steps_needed = max(0, (total_length - current_intersection) // (2 * n))

    results.append(steps_needed)

for result in results:
    print(result)
