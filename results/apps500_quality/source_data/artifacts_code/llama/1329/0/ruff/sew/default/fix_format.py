import math


def count_shichi_go_numbers(n):
    # Calculate N!
    factorial = math.factorial(n)

    # Function to count the number of divisors of a number
    def count_divisors(x):
        count = 0
        for i in range(1, 1 + int(math.sqrt(x))):
            if x % i == 0:
                if x / i == i:
                    count += 1
                else:
                    count += 2
        return count

    # Count the number of divisors of N! that are Shichi-Go numbers
    shichi_go_count = 0
    for i in range(1, n + 1):
        if 7 == count_divisors(i):
            if factorial % i == 0:
                shichi_go_count += 1

    return shichi_go_count


# Read input from standard input
n = int(input())

# Print the result
print(count_shichi_go_numbers(n))
