n, h, k = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
L = L[::-1]
p = 0
t = 0
while L:
	if h - p >= L[-1]:
		p += L.pop()
	if L:
		req = L[-1] - h + p
		inc = (req - 1) // k + 1
		t += inc
		p -= inc * k
		p = max(p, 0)

if p:
	t += 1 + (p - 1) // k

print(t)
