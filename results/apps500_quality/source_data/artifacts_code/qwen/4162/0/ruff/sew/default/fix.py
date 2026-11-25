def max_f(N, a):
    max_value=0
    for m in range(1, max(a) * N):
        f_m = sum(m % a_i for a_i in a)
        max_value = max(max_value, f_m)
    return max_value

# Read input
N = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
print(max_f(N, a))
