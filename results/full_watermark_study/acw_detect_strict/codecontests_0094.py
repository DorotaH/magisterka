from collections import Counter

t = int(input())

for _ in range(t):
	s = input()

	c = Counter(s)

	x = c["C"] + c["A"] == c["B"]
	print("YES" if x else "NO")
