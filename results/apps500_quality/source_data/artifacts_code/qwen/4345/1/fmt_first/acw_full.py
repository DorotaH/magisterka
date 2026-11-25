def split_sequence(n, a):
	increasing = []
	decreasing = []
	i, j = 0, n - 1

	while i <= j:
		if i == j:
			increasing.append(a[i])
			break
		if a[i] < a[i + 1]:
			increasing.append(a[i])
			i += 1
		elif a[j] < a[j - 1]:
			increasing.append(a[i])
			i += 1
		elif a[j] > a[j - 1]:
			decreasing.append(a[j])
			j -= 1
		else:
			return "NO"

	if not increasing or not decreasing:
		return "NO"

	result = [1 if x in increasing else 0 for x in a]
	return " ".join(map(str, result)) + "YES\n"


# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output result
print(split_sequence(n, a))
