import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
max_count = 0
current_count = 1

for i in range(1, n):
    if a[i] == a[i - 1] + 1:
        current_count += 1
    else:
        max_count = max(max_count, current_count)
        current_count = 1

max_count = max(max_count, current_count)
print(max_count)
