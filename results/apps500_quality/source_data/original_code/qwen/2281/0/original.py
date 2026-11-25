import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(range(1, n + 1)) + list(range(1, n + 1))
print(' '.join(map(str, a)))
