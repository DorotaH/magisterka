def can_build_string(s, t):
	s = list(s)
	t = list(t)
	t.reverse()
	for _ in range(2):
		for char in t:
			if s and s[-1] == char:
				s.pop()
			else:
				return False
	return not s


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	T = int(data[0])
	results = []

	index = 1
	for _ in range(T):
		s = data[index]
		t = data[1 + index]
		index += 2
		if can_build_string(s, t):
			results.append("YES")
		else:
			results.append("NO")

	for result in results:
		print(result)


if __name__ == "__main__":
	main()
