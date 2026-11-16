def sum_digits_single(x):
    ans = 0
    while x:
        ans = ans + x % 10
        x = x // 10
    return ans


def closest(x):
    ans = 0
    while 9 + ans * 10 <= x:
        ans = 9 + ans * 10
    return ans


def sum_digits_twoparts(N):
    A = closest(N)
    return sum_digits_single(A) + sum_digits_single(N - A)
