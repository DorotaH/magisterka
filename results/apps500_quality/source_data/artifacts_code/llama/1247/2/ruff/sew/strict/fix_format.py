from collections import Counter

s = input()
cnt = Counter(s)
odd = sum(count % 2 for count in cnt.values())

if not odd > 1:
    print("Second")
else:
    print("First")
