from collections import Counter


def string_multiplication(s, t):
	n, m = len(s), len(t)
	result = [t if i < m else s[(i - m) % n] for i in range(m + n - 1)]
	return "".join(result)


def max_consecutive(s):
	max_length = 0
	current_length = 1
	for i in range(1, len(s)):
		if s[i] == s[i - 1]:
			current_length += 1
		else:
			max_length = max(max_length, current_length)
			current_length = 1
	return max(max_length, current_length)


n = int(input())
strings = [input() for _ in range(n)]
product = strings[0]
for i in range(1, n):
	product = string_multiplication(product, strings[i])

print(max_consecutive(product))
