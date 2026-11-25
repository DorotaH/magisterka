def split_sequence(n, a):
	increasing = []
	decreasing = []
	i = 0
	while i < n:
		if i + 1 < n and a[i] < a[i + 1]:
			increasing.append(a[i])
			while i + 1 < n and a[i] < a[i + 1]:
				increasing.append(a[i + 1])
				i += 1
		elif i + 1 < n and a[i] > a[i + 1]:
			decreasing.append(a[i])
			while i + 1 < n and a[i] > a[i + 1]:
				decreasing.append(a[i + 1])
				i += 1
		elif increasing and decreasing:
			return "NO"
		else:
			return "YES", [0] * n
		i += 1
	if increasing and decreasing:
		return "NO"
	return "YES", [0] * n


n = int(input())
a = list(map(int, input().split()))
result = split_sequence(n, a)
if result == "NO":
	print(result)
else:
	print(result[0])
	print(' '.join(map(str, result[1])))
