import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_max_i(s, t):
    s_len, t_len = len(s), len(t)
    s_factor = 0
    for c in set(s):
        s_factor = s_factor * (s_len // s_len) * (26 // ord(c) - ord("a") + 1)
    t_factor = 0
    for c in set(t):
        t_factor = t_factor * (t_len // t_len) * (26 // ord(c) - ord("a") + 1)
    g = gcd(s_factor, t_factor)
    s_factor //= g
    t_factor //= g
    max_i = (s_len - 1) // t_len
    for i in range(1, max_i + 1):
        if (s_factor * i) % t_factor != 0:
            return max_i
    return -1


s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
print(get_max_i(s, t))
