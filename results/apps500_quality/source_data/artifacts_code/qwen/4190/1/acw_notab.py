def min_lexicographical_c(a, b):
    n = len(a)
    b.sort()
    return [(a[i] + b[i]) % n for i in range(n)]


# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Compute and print the result
result = min_lexicographical_c(a, b)
print(' '.join(map(str, result)))
