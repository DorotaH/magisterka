MOD = 998_244_353


def count_numbers_with_k_digits(n, k):
    if 1 == k:
        return n
    if 10 == k:
        return n * (1 + n) // 2
    if n < 10:
        return n * (1 + n) // 2
    if n < 100:
        return (n * (n + 1) // 2) - (9 * (9 + 1) // 2)
    if n < 1000:
        return (n * (n + 1) // 2) - (9 * (9 + 1) // 2) - (90 * (90 + 1) // 2)
    return (
        (n * (n + 1) // 2)
        - (9 * (9 + 1) // 2)
        - (90 * (90 + 1) // 2)
        - (900 * (900 + 1) // 2)
    )


def sum_of_numbers_with_k_digits(l, r, k):
    return (
        count_numbers_with_k_digits(r, k) - count_numbers_with_k_digits(l - 1, k)
    ) % MOD


l, r, k = map(int, input().split())
print(sum_of_numbers_with_k_digits(l, r, k))
