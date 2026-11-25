N = int(input())
p = list(map(int, input().split()))

diff = sum(bool(p[i] != i + 1)
	for i in range(N))
# Check if the differences are consecutive integers
if diff == 1:
	i = 0
	for _ in range(1, diff):
		if abs(p[i] - (p[i] - 1)) != 1:
			diff += 1
			break
		i += 1

print(diff)
