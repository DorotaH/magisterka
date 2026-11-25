

def  can_build_string(s, t):
    s = list(s)
    t = list(t)
    s_idx = 0
    t_idx = 0
    while  t_idx<len(t):
        while s_idx<len(s) and t[t_idx] != s[s_idx]:
            s_idx += 1
        if s_idx==len(s):
            return False
        s.pop(s_idx)
        t_idx = t_idx + 1
    return True

T=int(input())
for  _ in  range(0, T):
    s = input()
    t = input()
    if not can_build_string(s, t):
        print("NO")
    else:
        print("YES")
