n = int(input())
a = list(map(int, input().split()))

max_a = max(a[1:])
if a[0] <= 2 * max_a:
	print(0)
else:
	result = [1]
	total = a[0]
	i = 1
	while i < n:
		if max(a[1:]) <= a[i] and a[0] >= 2 * a[i]:
			result.append(i + 1)
			total += a[i]
		i += 1
	if total < (n * (1 + n)) // 2:
		print(0)
	else:
		print(len(result))
		print(" ".join(map(str, result)))
