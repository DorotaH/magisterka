from collections import Counter

s = input()
cnt = Counter(s)
odd = sum(count % 2 for count in cnt.values())

if odd > 1:
    print("First")
else:
    print("Second")
