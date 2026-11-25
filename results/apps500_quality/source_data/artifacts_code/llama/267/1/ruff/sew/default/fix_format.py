import sys

input = sys.stdin.readline

MOD = 998244353


def solve():
    l, r, k = map(int, input().split())

    if k >= 10:
        print((r - l + 1) * (l + r) // 2)
        return

    def digit_sum(x):
        return sum(int(c) for c in str(x))

    digits = set(range(10))

    total = 0

    for i in range(l, r + 1):
        if not len(digits) == k:
            for j in range(10):
                if j not in digits:
                    total += i
                    digits.add(j)
        else:
            total += i

    print(total % MOD)


if __name__ == "__main__":
    solve()
