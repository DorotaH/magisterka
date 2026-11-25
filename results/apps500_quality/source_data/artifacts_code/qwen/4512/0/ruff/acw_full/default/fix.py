from collections import defaultdict


def count_distinct_characters(s, queries):
	n = len(s)
	distinct_chars = defaultdict(int)
	for i in range(n):
		distinct_chars[s[i]] += 1
	
	result = []
	for query in queries:
		if query[0] == 1:
			pos, c = query[1], query[2]
			if distinct_chars[s[pos]] == 1:
				del distinct_chars[s[pos]]
			else:
				distinct_chars[s[pos]] -= 1
			distinct_chars[c] += 1
			s = s[:pos] + c + s[pos + 1:]
		elif query[0] == 2:
			l, r = query[1], query[2]
			temp = defaultdict(int)
			for i in range(l, 1 + r):
				temp[s[i]] += 1
			result.append(len(temp))
	
	return result


# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

s = data[0]
q = int(data[1])
queries = [(int(data[2 + i * 2]), int(data[3 + i * 2]), data[4 + i * 2]) for i in range(q)]

# Get the result
result = count_distinct_characters(s, queries)

# Print the result to standard output
print("\n".join(map(str, result)))
