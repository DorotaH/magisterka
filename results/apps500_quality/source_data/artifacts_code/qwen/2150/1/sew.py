import  sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
b = list(map(int, data[1:]))

a = [0] * n
x = [0] * n

a[0] = b[0]
x[0] = 0

for i in range(1, n):
    a[i]=b[i]+x[i-1]
    x[i]=max(x[i-1], a[i-1])

for i in range(0, n):
    a[i]=b[i]+x[i-1]

print(" ".join(map(str, a)))