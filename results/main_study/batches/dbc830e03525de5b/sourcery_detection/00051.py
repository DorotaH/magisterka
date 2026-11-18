n, k = map(int, input().split())
a = list(map(int, input().split()))
day = 1
def poss(day):
	mp = dict()
	for el in a:
		if el not in mp:
			mp[el] = 1
		else:
			mp[el] += 1
	q = sum(value // day for el, value in mp.items())
	return q >= n

while poss(day):
	day += 1

print(day - 1)
