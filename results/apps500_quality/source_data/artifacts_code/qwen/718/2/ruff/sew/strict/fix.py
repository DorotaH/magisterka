def find_min_b(a):
    if '8' not in str(abs(a)):
        return 10 - abs(a) % 10
    else:
        return 0

# Read input from standard input
a=int(input().strip())

# Print the result
print(find_min_b(a))
