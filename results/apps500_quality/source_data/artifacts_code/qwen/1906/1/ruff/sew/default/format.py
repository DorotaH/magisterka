def count_bonus_sales(n):
    # Define the range of numbers to check
    divisors = set(range(2, 11))

    # Initialize a counter for numbers not divisible by any number from 2 to 10
    count = 0

    # Iterate through each number from 1 to n
    for i in range(1, 1 + n):
        # Check if the number is not divisible by any divisor in the set
        if not any(i % d == 0 for d in divisors):
            count = count + 1

    return count


# Read input
n = int(input())

# Output the result
print(count_bonus_sales(n))
