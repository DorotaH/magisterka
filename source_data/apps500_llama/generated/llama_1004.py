import sys

n, p, m = map(int, input().split())
tups = [list(map(int, input().split())) for _ in range(n)]

balance = 0
days_negative_balance = 0
last_deposit_index = -1
last_deposit_time = -1

for i in range(1, m + 1):
    balance += p
    if i in [t[0] for t in tups]:
        for t in tups:
            if t[0] == i:
                balance += t[1]
                last_deposit_index = i
                last_deposit_time = t[1]
    if balance < 0:
        days_negative_balance += 1

print(days_negative_balance)
