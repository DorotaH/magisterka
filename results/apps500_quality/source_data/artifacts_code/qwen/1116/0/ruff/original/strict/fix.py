import sys


def can_paint_fence(r, b, k):
    if r == b:
        return "REBEL" if r % k == 0 else "OBEY"
    if k <= max(r, b):
        return "REBEL"
    if r % k == 0 or b % k == 0:
        return "OBEY"
    if (k % r == 0 and k % b != 0) or (k % r != 0 and k % b == 0):
        return "OBEY"
    return "REBEL"

input = sys.stdin.read
data = input().split()
T = int(data[0])
results = []

index = 1
for _ in range(T):
    r = int(data[index])
    b = int(data[index + 1])
    k = int(data[index + 2])
    index += 3
    results.append(can_paint_fence(r, b, k))

for result in results:
    print(result)
