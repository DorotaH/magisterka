import sys

a, b, c = map(int, input().split())

for i in range(1, 100000):
    if i % a == 0 and (i % b) == c:
        print('YES')
        sys.exit(0)
print('NO')
