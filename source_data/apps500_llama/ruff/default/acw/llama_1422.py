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
    return a * b // gcd(a, b)


def max_i():
    """Find the maximum value of i such that i copies of t is a substring of j copies of s"""
    max_i = 0
    n = len(s)
    m = len(t)
    t_count = {}

    # Count the frequency of each character in t
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    for _ in range(n):
        s_count = {}
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1

        found = not any(
            char not in s_count or s_count[char] < t_count[char] for char in t_count
        )
        if found:
            max_i += 1
        else:
            break

    # If the number of non-negative integers i satisfying the condition is infinite, print -1
    if max_i == 0:
        print(-1)
    else:
        # The maximum value of i is the LCM of the lengths of s and t
        print(lcm(n, m))


max_i()
