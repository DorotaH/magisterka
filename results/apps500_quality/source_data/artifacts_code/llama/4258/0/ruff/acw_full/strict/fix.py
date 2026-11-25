
A, B, T = map(int, input().split())
total_biscuits = 0
t = 0

while t <= T + 0.5:
	total_biscuits += B
	t += A
	A += 1

print(int(total_biscuits))
