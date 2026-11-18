
"""

b[i] = a[i] - i - 1

b[i] <= b[i+1] < 2b[i] + i - 1

sum(b) == r
"""


def solve(n, k):

    r = n - k * (k + 1) // 2
    if r < 0:
        return None

    b0 = r // k

    r -= b0 * k

    seq = k * [None]
    seq[0] = b0
    b = b0

    for i in range(1, k):
        bn = 2 * b + i - 1

        h = r // (k - i)
        if h > 0:
            if h + b > bn:
                h = bn - b
            r -= h * (k - i)
            b = h + b
        seq[i] = b
    return None if r != 0 else [i + b + 1 for i, b in enumerate(seq)]


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    if res is None:
        print('NO')
    else:
        print('YES')
        print(*res)


main()
