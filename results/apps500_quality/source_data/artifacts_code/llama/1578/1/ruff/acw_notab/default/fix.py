n = int(input())


def find_max_sum(n):
    max_sum = 0
    for p in range(1, 1 + n):
        m = n // p
        for q in range(p, 1 + n):
            M = (q - 1) // p
            max_sum = max(max_sum, m + M)
    return n * max_sum


print(find_max_sum(n))
