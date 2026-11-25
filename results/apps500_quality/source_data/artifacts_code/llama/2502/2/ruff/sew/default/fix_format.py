from math import gcd

s = input().strip()
t = input().strip()


def find_gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the least common multiple of a and b"""
    return b * a // gcd(a, b)


def max_i():
    """Find the maximum value of i such that i copies of t is a substring of j copies of s"""
    max_i, n = 0, len(s)
    m, t_count = len(t), {}

    # Count the frequency of each character in t
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    for i in range(n):
        s_count = {}
        for char in s:
            s_count[char] = 1 + s_count.get(char, 0)

        found = True
        for char in t_count:
            if char not in s_count or t_count[char] > s_count[char]:
                found = False
                break

        if not found:
            break
        else:
            max_i += 1

    # If the number of non-negative integers i satisfying the condition is infinite, print -1
    if not max_i == 0:
        print(lcm(n, m))
    else:
        # The maximum value of i is the LCM of the lengths of s and t
        print(-1)


max_i()
