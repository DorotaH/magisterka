from collections import Counter

s = input()
char_count = Counter(s)

odd_count = sum(val % 2 for val in char_count.values())

if not odd_count <= 1:
    print("Second")
else:
    print("First")
