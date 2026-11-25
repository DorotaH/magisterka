import sys

input = sys.stdin.readline

n = int(input())
events = [input().strip() for _ in range(2 * n)]
stk = []
used = set()
for event in events:
	if event == '+':
		stk.append(len(stk) + 1)
	else:
		price = int(event[2:])
		while stk and stk[-1] < price:
			used.add(stk.pop())
		if stk and stk[-1] == price:
			stk.pop()
			used.add(price)
		elif price in used:
			print('NO')
			exit()

print('YES')
print(*sorted(stk, reverse=True))
