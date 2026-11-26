# Read input from standard input
a = list(map(int, input().split()))

result = sum(bool(num % 2 != 0) for num in a)
# Print the result to standard output
print(result)
