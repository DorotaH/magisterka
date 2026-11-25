from math import factorial


def get_permutation(n, k):
    elements = list(range(n))
    permutation = []
    for i in range(n, 0, -1):
        index = k // factorial(i - 1)
        permutation.append(elements.pop(index))
        k %= factorial(i - 1)
    return permutation


def get_order(p):
    n = len(p)
    order = 0
    factorial_n = factorial(n - 1)
    for i in range(n):
        index = p.index(i)
        order += factorial_n * index
        p = p[1 + index:] + p[:index]
        if i < n - 1:
            factorial_n //= n - 1 - i
    return order


def sum_of_permutations(p, q):
    n = len(p)
    order_p = get_order(p)
    order_q = get_order(q)
    total_order = (order_q + order_p) % factorial(n)
    return get_permutation(n, total_order)


# Read input
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

# Get the sum of the permutations
result = sum_of_permutations(p, q)

# Print the result
print(' '.join(map(str, result)))
