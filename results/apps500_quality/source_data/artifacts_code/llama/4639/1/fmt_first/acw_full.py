import sys


def get_string(n, k):
	result = (n - 2) * ["a"]
	b_count = 2
	for i in range(n - 2, -1, -1):
		if k > 0:
			if k >= (n - i - 1) * (n - i) // 2:
				result.insert(i, "b")
				b_count -= 1
				k -= (n - i - 1) * (n - i) // 2
			elif k >= (n - i - 1) * (n - i) // 2 - (n - i - 1) * (n - i) // 2:
				result.insert(i, "b")
				b_count -= 1
				k -= (n - i - 1) * (n - i) // 2 - (n - i - 1) * (n - i) // 2
		else:
			break
	result = "".join(result)
	return result.replace("0", "a")


t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	print(get_string(n, k))
