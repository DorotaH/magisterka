import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:]))

a.sort()

max_comb = 0
best_pair = (0, 0)

for i in range(n):
    for j in range(i + 1, n):
        comb = (a[i] - 1) * a[i] // 2
        if comb > max_comb:
            max_comb = comb
            best_pair = (a[i], a[j])

print(best_pair[0], best_pair[1])
