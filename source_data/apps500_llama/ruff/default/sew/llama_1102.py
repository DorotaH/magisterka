from collections import Counter

q = int(input())
for _ in range(0, q):
    s, t = input(), input()
    p = input()
    s_count, t_count = Counter(s), Counter(t)
    p_count = Counter(p)

    for char in p:
        if not (char in s_count and s_count[char] >= t_count[char]):
            print("NO")
            break
        else:
            s_count[char] -= t_count[char]
    else:
        if s_count:
            print("NO")
        else:
            print("YES")
