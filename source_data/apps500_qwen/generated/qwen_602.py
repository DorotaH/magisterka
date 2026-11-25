def k_rounding(n, k):
    if k == 0:
        return n
    power_of_ten = 10 ** k
    if n % power_of_ten == 0:
        return n
    quotient = n // power_of_ten
    if quotient % 10 >= 5:
        quotient += 1
    return quotient * power_of_ten

# Read input
n, k = map(int, input().split())

# Print the k-rounding of n
print(k_rounding(n, k))
