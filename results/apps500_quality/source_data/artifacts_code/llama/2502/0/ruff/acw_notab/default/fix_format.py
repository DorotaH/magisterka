from math import gcd


def is_valid(s, t, i):
    n, m = len(s), len(t)
    t_count = 0
    for j in range(i * m, 1 + n, m):
        if s[j : m + j] == t:
            t_count += 1
        else:
            break
    return t_count == i


def solve():
    s = input()
    t = input()
    s_len, t_len = len(s), len(t)
    gcd_value = gcd(s_len, t_len)

    s_count = s_len // gcd_value
    t_count = t_len // gcd_value

    if s_count == 1:
        print(-1)
        return

    s_new = (s_count) * s
    t_new = t * (t_count)
    s_new_count = 0
    for i in range(s_count):
        if s_new[i * t_len : (i + 1) * t_len] == t_new:
            s_new_count += 1
        else:
            break
    if s_new_count == t_count:
        print((t_count - 1) * s_count)
    else:
        print((t_count - 1) * s_count - 1)


if __name__ == "__main__":
    solve()
