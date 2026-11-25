import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

results = list()

for _ in range(t):
    n, k = int(data[index]), int(data[index + 1])
    l1, r1 = int(data[index + 2]), int(data[index + 3])
    l2, r2 = int(data[index + 4]), int(data[index + 5])
    index += 6

    total_length, current_intersection = (
        (r1 - l1 + 1) * (r2 - l2 + 1),
        (min(r1, r2) - max(l1, l2) + 1),
    )
    steps_needed = max(0, (total_length - current_intersection) // (2 * n))

    results.append(steps_needed)

for result in results:
    print(result)
