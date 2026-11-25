def is_unique_crossword(n, x, a):
    total_length = sum(a)
    if total_length != x:
        return "NO"

    num_gaps = 1 + n
    return "NO" if x - total_length != num_gaps - 1 else "YES"


# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(is_unique_crossword(n, x, a))
