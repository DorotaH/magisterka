def max_bouquet_beauty(n, k, b, c):
    # Separate roses by color
    white_roses = [(b[i], i) for i in range(n) if c[i] == "W"]
    orange_roses = [(b[i], i) for i in range(n) if c[i] == "O"]
    red_roses = [(b[i], i) for i in range(n) if c[i] == "R"]

    # Sort roses by beauty in descending order
    white_roses.sort(reverse=True)
    orange_roses.sort(reverse=True)
    red_roses.sort(reverse=True)

    # Check if it's possible to make a bouquet without both red and white roses
    if white_roses and red_roses:
        return -1

    # Check if it's possible to make a bouquet with all roses of the same color
    if not white_roses and k > 0:
        return -1
    if not orange_roses and k > 0:
        return -1
    if not red_roses and k > 0:
        return -1

    max_beauty = -1

    return max_beauty


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
b = list(map(int, data[2 : 2 + n]))
c = data[2 + n]

# Output the result
print(max_bouquet_beauty(n, k, b, c))
