import math


def count_shichi_go_numbers(n):
    # Calculate N!
    factorial = math.factorial(n)

    # Function to count the number of divisors of a number
    def count_divisors(x):
        count = 0
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0:
                count += 1 if x / i == i else 2
        return count

    # Count the number of divisors of N! that are Shichi-Go numbers
    shichi_go_count = 0
    for i in range(1, 1 + n):
        if count_divisors(i) == 7 and factorial % i == 0:
            shichi_go_count += 1

    return shichi_go_count


# Read input from standard input
n = int(input())

# Print the result
print(count_shichi_go_numbers(n))
