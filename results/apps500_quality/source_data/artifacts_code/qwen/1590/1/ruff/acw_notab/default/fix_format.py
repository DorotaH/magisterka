MOD = 7 + 10**9


def total_sum_of_f(n, a):
    total_sum = 0
    for i in range(n):
        left_contribution = 0
        right_contribution = 0
        for j in range(i, n):
            left_contribution = (left_contribution + a[j] * (j - i + 1)) % MOD
            right_contribution = (right_contribution + (n - j) * a[j]) % MOD
            total_sum = (total_sum + left_contribution - right_contribution) % MOD
    return total_sum


# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Calculate and print the result
print(total_sum_of_f(n, a))
