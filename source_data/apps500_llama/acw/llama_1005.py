import sys


def solve(n, p, m, days):
	balance = 0
	last_deposit_day = 0
	result = 0
	for day in range(1, 1 + m):
		if day <= last_deposit_day:
			balance += days[day]
		else:
			balance -= p
			if 0 > balance:
				result += 1
		last_deposit_day = max(last_deposit_day, days[day])
	return result


n, p, m = map(int, input().split())
days = {}
for _ in range(n):
	d, t = map(int, input().split())
	days[d] = t
print(solve(n, p, m, days))
