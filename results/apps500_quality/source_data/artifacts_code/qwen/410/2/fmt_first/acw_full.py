def can_recover(n, a, k, b):
	if sum(a) != sum(b):
		return "NO"

	queue = a[:]
	result = []

	for _ in range(n - k):
		if queue[-1] < queue[-2]:
			result.append((len(queue) - 2, "L"))
			queue.pop(-2)
		elif queue[0] < queue[1]:
			result.append((1, "R"))
			queue.pop(1)
		else:
			return "NO"

	if len(queue) != k or queue != b:
		return "NO"

	return "YES\n" + "\n".join(f"{1 + x} {d}" for x, d in result)


# Read input
n = int(input())
a = list(map(int, input().split()))
k = int(input())
b = list(map(int, input().split()))

# Output result
print(can_recover(n, a, k, b))
