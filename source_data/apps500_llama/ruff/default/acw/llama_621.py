import sys

n, m = map(int, input().split())
diff = abs(n - m)
result = m - diff
if diff == 0:
    result = m
    diff = 1
while result > 0 and result < n:
    if diff > abs(result - m):
        result -= 1
    else:
        break
print(result)
