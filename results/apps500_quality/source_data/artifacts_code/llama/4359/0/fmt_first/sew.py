import sys

A, B, C, D, E = map(int, sys.stdin.readline().split())
orders = [
    (A, 0),
    (B, 10),
    (C, 10 * (B + 1) + 7),
    (E, 10 * (C + 7) + 120),
    (D, 10 * (E + 120) + 35),
]

time = 0
for i in range(len(orders)):
    time = orders[i][0] + max(0, (orders[i][1] - time) // 10 * 10)

print(time)