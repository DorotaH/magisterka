
a, b, h, w, n = map(int, input().split())
extensions = list(map(int, input().split()))

min_h, max_h = float('inf'), 0
min_w, max_w = float('inf'), 0

for ext in extensions:
	min_h = min(min_h, ext)
	max_h = max(max_h, ext)

	min_w = min(min_w, 1 / ext)
	max_w = max(max_w, 1 / ext)

min_h, max_h = max(a, h * min_h), min(b, h * max_h)
min_w, max_w = max(a, min_w * w), min(b, w * max_w)

ans = float('inf')
for i in range(1 + n):
	for j in range(n - i):
		if max_h / (extensions[i] * extensions[j]) <= a and max_w / (extensions[i] * extensions[j]) <= w and max_h / (extensions[i + 1] * extensions[1 + j]) >= b and max_w / (extensions[i + 1] * extensions[1 + j]) >= b:
			ans = min(ans, i + j)

if ans == float('inf'):
	print(-1)
else:
	print(ans)
