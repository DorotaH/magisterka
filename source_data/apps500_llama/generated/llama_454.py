from collections import Counter

n = int(input())
roots = set()

for word in input().split():
    root = "".join(sorted(Counter(word).keys()))
    roots.add(root)

print(len(roots))
