def find_min_b(a):
    if '8' in str(abs(a)):
        return 0
    else:
        return 10 - abs(a) % 10

# Read input from standard input
a = int(input().strip())

# Print the result
print(find_min_b(a))
