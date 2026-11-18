n, m, k = list(map(int, input().split()))
x, s = list(map(int, input().split()))
t = list(map(int, input().split()))
pr = list(map(int, input().split()))
t2 = list(map(int, input().split()))
pr2 = list(map(int, input().split()))
minans = 10**20
mass1 = [(pr[i], t[i]) for i in range(m)]
mass1.sort()
mass1 = mass1 + [(0, x)]
pr2 = [0] + pr2
t2 = [0] + t2
uk1 = len(mass1) - 1
uk2 = 0
maxw = 0
for uk1 in range(len(mass1) - 1, -1, -1):
	if (mass1[uk1][0] > s):
		continue
	while (len(pr2) > uk2 and pr2[uk2] + mass1[uk1][0] <= s):
		maxw = max(maxw, t2[uk2])
		uk2 += 1
	uk2 -= 1
	minans = min(minans, (n - maxw) * mass1[uk1][1])
print(minans)
