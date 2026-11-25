from collections import Counter

s = input().strip()
q = int(input().strip())

# Initialize a list to store the Counter of characters for each prefix of the string
prefix_counters = [Counter()]
for char in s:
	prefix_counters.append(Counter(prefix_counters[-1]))
	prefix_counters[-1][char] += 1

# Process each query
for _ in range(q):
	query = input().strip().split()
	if query[0] == '1':
		pos, c = int(query[1]) - 1, query[2]
		prefix_counters[pos + 1][s[pos]] -= 1
		if prefix_counters[pos + 1][s[pos]] == 0:
			del prefix_counters[pos + 1][s[pos]]
		prefix_counters[pos + 1][c] += 1
		s = s[:pos] + c + s[pos + 1:]
	elif query[0] == '2':
		l, r = int(query[1]) - 1, int(query[2])
		print(len(prefix_counters[1 + r] - prefix_counters[l]))
