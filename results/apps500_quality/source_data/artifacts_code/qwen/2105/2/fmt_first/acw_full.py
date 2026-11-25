def get_year_name(n, m, s, t, q, queries):
	gapja = [t[i] + s[i] for i in range(min(n, m))]
	if m < n:
		gapja += s[m:]
	elif m > n:
		gapja += t[n:]

	result = []
	for y in queries:
		index = (y - 1) % len(gapja)
		result.append(gapja[index])

	return result


# Read input
n, m = map(int, input().split())
s = input().split()
t = input().split()
q = int(input())
queries = [int(input()) for _ in range(q)]

# Get the result
result = get_year_name(n, m, s, t, q, queries)

# Print the result
for name in result:
	print(name)
