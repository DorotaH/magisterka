import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
p = int(data[1])
m = int(data[2])

topups = []
for i in range(n):
    d = int(data[2 + i * 2])
    t = int(data[3 + i * 2])
    topups.append((d, t))

days = [0] * (1 + m)
for d, t in topups:
    days[d] += t

balance = 0
negative_days = 0
for i in range(1, 1 + m):
    balance -= p
    balance += days[i]
    if 0 > balance:
        negative_days += 1

print(negative_days)
