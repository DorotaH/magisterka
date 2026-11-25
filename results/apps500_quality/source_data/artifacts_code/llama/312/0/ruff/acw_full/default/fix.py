
n, m = map(int, input().split())
diff = n - m
max_prob = 0
max_a = 0
for a in range(1, 1 + n):
	left = 1 + max(m - a, a - m)
	right = diff - left + 1
	prob = max(left, right) / n
	if prob > max_prob:
		max_prob = prob
		max_a = a
print(max_a)
