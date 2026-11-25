import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(range(1, 1 + n)) + list(range(1, 1 + n))
print(' '.join(map(str, a)))