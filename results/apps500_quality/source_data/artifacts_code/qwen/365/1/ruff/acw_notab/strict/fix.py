def is_unique_crossword(n, x, a):
    # Calculate the total length of the segments
    total_length = sum(a)

    # Check if the total length matches the given length
    if total_length != x:
        return "NO"

    # Check if there is exactly one segment of length x
    if len(a) == 1 and a[0] == x:
        return "YES"

    # Check if there is exactly one segment of length x and the rest are of length 1
    if len(a) == 2 and a[0] == 1 and a[1] == x - 1:
        return "YES"
    if len(a) == 2 and a[1] == 1 and a[0] == x - 1:
        return "YES"

    # Check if there is exactly one segment of length x and the rest are of length 1
    if len(a) > 2 and a[0] == 1 and a[-1] == 1 and sum(a[1:-1]) == x - 2:
        return "YES"
    return "NO"


# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(is_unique_crossword(n, x, a))
