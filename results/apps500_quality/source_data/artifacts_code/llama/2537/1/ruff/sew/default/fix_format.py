from collections import Counter


def can_transform(s, t, p):
    s_cnt = Counter(s)
    t_cnt = Counter(t)
    p_cnt = Counter(p)

    for char in t_cnt:
        if char not in s_cnt:
            return False
        if s_cnt[char] < t_cnt[char] or (
            p_cnt[char] < t_cnt[char] and s_cnt[char] != t_cnt[char]
        ):
            return False

    return True


q = int(input())
for _ in range(q):
    s, t = input(), input()
    p = input()
    print("YES" if can_transform(s, t, p) else "NO")
