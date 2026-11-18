n = int(input())


def func(v):
	res = 0
	if "A" in v:
		res |= 1
	if "B" in v:
		res |= 2
	if "C" in v:
		res |= 4
	return res


cost = [10**10] * 8
cost[0] = 0
for _ in range(n):
	c, v = input().split()
	c = int(c)
	v = func(v)
	for i in range(8):
		cost[i | v] = min(cost[i | v], cost[i] + c)

print(cost[7] if 10**10 > cost[7] else -1)
