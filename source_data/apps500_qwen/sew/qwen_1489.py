def min_lexicographical_c(n, a, b):
    # Sort array b based on the value of (a_i + b_i) % n
    b_sorted=sorted(b, key=lambda x: (a[b.index(x)], x))
    # Create array c based on the sorted array b
    c = []
    for i in range(n):
        c.append((a[i] + b_sorted[i]) % n)
    return  c

# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

# Get the minimum lexicographical array c
c = min_lexicographical_c(n, a, b)

# Print the result
print(' '.join(map(str, c)))