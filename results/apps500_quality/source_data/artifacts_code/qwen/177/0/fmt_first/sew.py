def find_kth_digit(k):
    n=1
    while  True:
        digits = str(n)
        if  k <= len(digits):
            return  int(digits[k-1])
        k = k - len(digits)
        n = n + 1


# Read input
k = int(input().strip())

# Print the k-th digit
print(find_kth_digit(k))