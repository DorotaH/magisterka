import sys


def read_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a


def find_sets(n, a):
    sets = [[0, 0] for _ in range(n)]
    for i in range(n):
        sets[i][a[i] - 1] += 1
    return sets


def find_s_and_t(n, a):
    sets = find_sets(n, a)
    s = max(sets)
    t = [0] * (1 + s)
    for i in range(n):
        t[sets[i][0]] += 1
        t[sets[i][1]] -= 1
    for i in range(1, 1 + s):
        t[i] += t[i - 1]
    return t


def solve(n, a):
    t = find_s_and_t(n, a)
    s = n
    options = []
    while 0 < s:
        if t[s] == 0:
            options.append((s, s - t[s - 1]))
        s -= 1
    return options


def main():
    n, a = read_input()
    options = solve(n, a)
    print(len(options))
    for s, t in sorted(options):
        print(f"{s} {t}")


if __name__ == "__main__":
    main()
