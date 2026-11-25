from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    cnt = Counter(s)
    odd_count = sum(1 for c in cnt.values() if 0 != c % 2)

    if not odd_count > 1:
        res = "".join(c * (cnt[c] // 2) for c in s)
        print(res)
    else:
        print(-1)
