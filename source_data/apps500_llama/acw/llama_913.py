def solve():
	n, x = map(int, input().split())
	s = input()

	prefix_balance = 0
	max_balance = 0
	max_balance_at = 0
	count = 0
	for i in range(n):
		if s[i] == '0':
			prefix_balance += 1
		else:
			prefix_balance -= 1
		if prefix_balance == x:
			count += 1
		if prefix_balance > max_balance:
			max_balance = prefix_balance
			max_balance_at = i + 1

	if prefix_balance == x:
		count += 1

	if max_balance_at % n == 0:
		print(-1)
	else:
		print(count)


t = int(input())
for _ in range(t):
	solve()
