import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
p = int(data[1])
m = int(data[2])

topups = []
for i in range(n):
    d = int(data[2 + 2 * i])
    t = int(data[3 + 2 * i])
    topups.append((d, t))

days = [0] * (m + 1)
for d, t in topups:
    days[d] += t

balance = 0
negative_days = 0
for i in range(1, m + 1):
    balance -= p
    balance += days[i]
    if balance < 0:
        negative_days += 1

print(negative_days)
