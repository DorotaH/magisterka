def find_fixed_errors(n, a, b, c):
    # Find the error that disappeared first
    first_fixed = set(a) - set(b)
    first_fixed = list(first_fixed)[0]

    # Find the error that disappeared second
    second_fixed = set(b) - set(c)
    second_fixed = list(second_fixed)[0]

    return first_fixed, second_fixed


# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Find and print the fixed errors
first_fixed, second_fixed = find_fixed_errors(n, a, b, c)
print(first_fixed, second_fixed)
