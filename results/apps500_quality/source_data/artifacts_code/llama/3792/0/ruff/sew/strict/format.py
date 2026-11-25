import sys


def read_int():
    return int(sys.stdin.readline().rstrip("\n"))


def read_ints():
    return map(int, sys.stdin.readline().rstrip("\n").split())


def read_int_list():
    return list(map(int, sys.stdin.readline().rstrip("\n").split()))


def solve():
    n, k = read_ints()
    s = sys.stdin.readline().rstrip("\n")
    t = sys.stdin.readline().rstrip("\n")

    if not s[0] == t[0]:
        for i in range(n):
            if s[i] != t[i]:
                return k * (i + 1)

        return k * (n + 1)

    else:
        max_len = 0
        for i in range(n):
            if s[i] == t[i]:
                max_len += 1
            else:
                break

        max_c = (k + 1) * max_len

        for i in range(n):
            if s[i] != t[i]:
                max_c += (k - 1) * (i - max_len + 1)

        return max_c


if __name__ == "__main__":
    print(solve())
