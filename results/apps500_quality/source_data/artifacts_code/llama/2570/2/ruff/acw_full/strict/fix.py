

def can_rearrange(a, b):
	"""Check if one can rearrange the elements of array b so that a[i] + b[i] <= x for each i."""
	n = len(a)
	i, j = 0, n - 1
	for k in range(n - 1, -1, -1):
		if b[k] + a[k] > b[-1]:
			return "No"
		if a[k] <= b[i]:
			i += 1
		else:
			j -= 1
			b[i], b[j] = b[j], b[i]
			if a[k] + b[j] > b[-1]:
				return "No"
	return "Yes"


t = int(input())
for _ in range(t):
	n, x = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	print(can_rearrange(a, b))
