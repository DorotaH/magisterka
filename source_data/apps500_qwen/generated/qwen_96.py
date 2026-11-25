import sys
input = sys.stdin.read
data = input().split()

a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])

max_value = max(a * c, a * d, b * c, b * d)
print(max_value)
