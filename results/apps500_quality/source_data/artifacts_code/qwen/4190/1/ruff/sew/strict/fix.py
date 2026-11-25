def  min_lexicographical_c(a, b):
    n = len(a)
    b.sort()
    c = [(a[i] + b[i]) % n for i in range(n)]
    return  c

# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Compute and print the result
result = min_lexicographical_c(a, b)
print(' '.join(map(str, result)))
