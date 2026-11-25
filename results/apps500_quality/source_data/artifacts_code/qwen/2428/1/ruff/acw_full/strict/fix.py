def can_build(s, t):
	i, j = 0, 0
	while i < len(s) and len(t) > j:
		if s[i] == t[j]:
			j += 1
		i += 1
	return j == len(t)


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	T = int(data[0])
	results = []

	index = 2
	for _ in range(T):
		s = data[index]
		t = data[1 + index]
		index += 2
		if can_build(s, t):
			results.append("YES")
		else:
			results.append("NO")

	for result in results:
		print(result)


if __name__ == "__main__":
	main()
