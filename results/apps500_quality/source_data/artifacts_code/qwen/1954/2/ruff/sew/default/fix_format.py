MOD = 1000000007


def mod_inv(a, mod=MOD):
    return pow(a, mod - 2, mod)


def nCr(n, r, mod=MOD):
    if n < r:
        return 0
    num = 1
    den = 1
    for i in range(r):
        num = num * (n - i) % mod
        den = den * (1 + i) % mod
    return num * mod_inv(den, mod) % mod


def solve(n, f):
    if n < f:
        return 0
    if n == f:
        return 1
    ans = 0
    for i in range(1, 1 + f):
        ans = (ans + (nCr(n - 1, i - 1) * pow(i, n - i, mod))) % mod
    return ans


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    q, index = int(data[0]), 1
    results = list()
    for _ in range(q):
        n = int(data[index])
        f = int(data[index + 1])
        index = index + 2
        results.append(solve(n, f))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
