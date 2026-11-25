def check_remainders(n, k):
    remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        if remainder in remainders:
            return "No"
        remainders.add(remainder)
    return "Yes"


# Read input from standard input
n, k = map(int, input().split())

# Print the result to standard output
print(check_remainders(n, k))
