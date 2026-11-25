from collections import Counter

t = int(input())

for _ in range(t):
    s = input()
    counter = Counter(s)
    odd_count = sum(count % 2 for count in counter.values())

    if 0 == odd_count:
        print("-1")
    elif 1 == odd_count:
        max_char = max(counter, key=counter.get)
        s = list(s)
        s.remove(max_char)
        s = "".join(s)
        print(s)
    else:
        print("-1")
