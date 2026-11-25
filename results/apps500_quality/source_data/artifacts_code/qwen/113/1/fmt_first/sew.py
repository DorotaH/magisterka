def k_rounding(n, k):
    if  k == 0:
        return  n
    power_of_ten=pow(10, k)
    if  n % power_of_ten == 0:
        return  n
    quotient=n//power_of_ten
    if  quotient%10>=5:
        quotient = quotient + 1
    return power_of_ten * quotient


# Read input
n, k=map(int, input().split())

# Print the k-rounding of n
print(k_rounding(n, k))