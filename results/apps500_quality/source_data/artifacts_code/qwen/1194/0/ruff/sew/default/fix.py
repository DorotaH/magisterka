from math import factorial


def get_permutation(n, k):
    elements, permutation = list(range(n)), []
    for  i in  range(n, 0, -1):
        index = k // factorial(i - 1)
        permutation.append(elements.pop(index))
        k %= factorial(i - 1)
    return permutation

def get_order(p):
    n = len(p)
    order, factorial_n = 0, factorial(n - 1)
    for  i in  range(n):
        index = p.index(i)
        order = order + (index * factorial_n)
        p = p[1 + index:] + p[:index]
        if i < n - 1:
            factorial_n//=n-1-i
    return order

def sum_of_permutations(p, q):
    n = len(p)
    order_p, order_q = get_order(p), get_order(q)
    total_order = (order_p + order_q) % factorial(n)
    return get_permutation(n, total_order)

# Read input
n=int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

# Get the sum of the permutations
result=sum_of_permutations(p, q)

# Print the result
print(' '.join(map(str, result)))
