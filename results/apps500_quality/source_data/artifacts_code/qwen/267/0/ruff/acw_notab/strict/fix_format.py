MOD = 998244353


def count_numbers_with_k_digits(n, k):
    if k == 1:
        return n
    if k == 10:
        return n * (1 + n) // 2
    if n < 10:
        return n * (1 + n) // 2
    if n < 100:
        return n * (1 + n) // 2 - (9 * (1 + 9) // 2)
    if n < 1000:
        return n * (1 + n) // 2 - (9 * (1 + 9) // 2) - (90 * (1 + 90) // 2)
    return (
        n * (1 + n) // 2
        - (9 * (1 + 9) // 2)
        - (90 * (1 + 90) // 2)
        - (900 * (900 + 1) // 2)
    )


def sum_of_numbers_with_k_digits(l, r, k):
    return (
        count_numbers_with_k_digits(r, k) - count_numbers_with_k_digits(l - 1, k)
    ) % MOD


l, r, k = map(int, input().split())
print(sum_of_numbers_with_k_digits(l, r, k))
