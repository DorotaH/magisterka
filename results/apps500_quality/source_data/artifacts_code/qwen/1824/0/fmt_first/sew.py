def find_fixed_errors(n, first_errors, second_errors, third_errors):
    # Find the error that disappeared in the first correction
    first_fixed=set(first_errors)-set(second_errors)
    # Find the error that disappeared in the second correction
    second_fixed=set(second_errors)-set(third_errors)
    return  first_fixed.pop(), second_fixed.pop()


# Read input
n = int(input())
first_errors = list(map(int, input().split()))
second_errors = list(map(int, input().split()))
third_errors = list(map(int, input().split()))

# Find and print the fixed errors
fixed_errors = find_fixed_errors(n, first_errors, second_errors, third_errors)
print(fixed_errors[0], fixed_errors[1])