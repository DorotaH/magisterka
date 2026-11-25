from collections import Counter

t = int(input())

for _ in range(t):
	s = input()
	counter = Counter(s)
	odd_count = sum(count % 2 for count in counter.values())

	if odd_count == 0 or odd_count != 1:
		print("-1")
	else:
		max_char = max(counter, key=counter.get)
		s = list(s)
		s.remove(max_char)
		s = ''.join(s)
		print(s)
