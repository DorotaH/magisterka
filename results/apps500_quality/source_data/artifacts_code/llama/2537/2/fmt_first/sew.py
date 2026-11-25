from collections import Counter

def check_string(s, t, p):
    s_cnt = Counter(s)
    t_cnt = Counter(t)
    p_cnt = Counter(p)

    for char in t:
        if  char not  in s_cnt or  t_cnt[char] > s_cnt[char]:
            if char not in p_cnt or t_cnt[char] > p_cnt[char]:
                return  False
            s_cnt[char] += p_cnt[char] - t_cnt[char]

    return True


q = int(input())
for _ in range(q):
    s, t = input(), input()
    p=input()
    print("YES" if  check_string(s, t, p) else "NO")
