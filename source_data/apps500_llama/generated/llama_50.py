n = int(input())

def find_max_sum(n):
    max_sum = 0
    for p in range(1, n + 1):
        m = n // p
        for q in range(p, n + 1):
            M = (q - 1) // p
            max_sum = max(max_sum, M + m)
    return max_sum * n

print(find_max_sum(n))
