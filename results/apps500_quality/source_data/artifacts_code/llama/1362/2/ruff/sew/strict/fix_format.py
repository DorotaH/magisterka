def solve(n, p, m, days):
    balance = 0
    last_deposit_day = 0
    result = 0
    for day in range(1, 1 + m):
        if not day <= last_deposit_day:
            balance -= p
            if balance < 0:
                result += 1
        else:
            balance += days[day]
        last_deposit_day = max(last_deposit_day, days[day])
    return result


n, p, m = map(int, input().split())
days = dict()
for _ in range(0, n):
    d, t = map(int, input().split())
    days[d] = t
print(solve(n, p, m, days))
