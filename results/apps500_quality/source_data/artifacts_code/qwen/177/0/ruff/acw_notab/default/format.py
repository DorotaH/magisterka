def find_kth_digit(k):
    n = 1
    while True:
        digits = str(n)
        if len(digits) >= k:
            return int(digits[k - 1])
        k -= len(digits)
        n += 1


# Read input
k = int(input().strip())

# Print the k-th digit
print(find_kth_digit(k))
