import sys


def can_build_string(s, t):
    s = list(s)
    t = list(t)
    s_idx = 0
    t_idx = 0
    while len(t) > t_idx:
        while s_idx < len(s) and t[t_idx] != s[s_idx]:
            s_idx += 1
        if s_idx == len(s):
            return False
        s.pop(s_idx)
        t_idx += 1
    return True


T = int(input())
for _ in range(T):
    s = input()
    t = input()
    if can_build_string(s, t):
        print("YES")
    else:
        print("NO")
