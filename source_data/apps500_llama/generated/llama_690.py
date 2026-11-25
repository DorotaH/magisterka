from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    cnt = Counter(s)
    odd_count = sum(1 for c in cnt.values() if c % 2 != 0)

    if odd_count > 1:
        print(-1)
    else:
        res = ''.join(c * (cnt[c] // 2) for c in s)
        print(res)
