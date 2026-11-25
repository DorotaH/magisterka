from collections import Counter

n = int(input())
words = input().split()
roots = set()

for word in words:
	root = ''.join(sorted(set(word)))
	roots.add(root)

print(len(roots))
