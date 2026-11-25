from collections import Counter

q = int(input())
for _ in range(q):
	s = input()
	t = input()
	p = input()
	s_count = Counter(s)
	t_count = Counter(t)
	p_count = Counter(p)

	for char in p:
		if char in s_count and s_count[char] >= t_count[char]:
			s_count[char] -= t_count[char]
		else:
			print("NO")
			break
	else:
		if not s_count:
			print("YES")
		else:
			print("NO")
