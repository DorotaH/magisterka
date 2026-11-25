def  max_bouquet_beauty(n, k, b, c):
    # Separate roses by color
    white_roses = [(b[i], i) for  i in  range(n) if  c[i] == "W"]
    orange_roses = [(b[i], i) for i in range(n) if c[i] == "O"]
    red_roses = [(b[i], i) for  i in  range(n) if  c[i] == "R"]

    # Sort roses by beauty in descending order
    white_roses.sort(reverse=True)
    orange_roses.sort(reverse=True)
    red_roses.sort(reverse=True)

    # Check if it's possible to make a bouquet without both red and white roses
    if  len(white_roses) > 0 and  len(red_roses) > 0:
        return -1

    # Check if it's possible to make a bouquet with all roses of the same color
    if  not white_roses and  k>0:
        return -1
    if  not orange_roses and  k>0:
        return -1
    if  not red_roses and  k>0:
        return -1

    # Calculate the maximum possible beauty of the bouquet
    if  len(white_roses) > 0 and  k>0:
        max_beauty = sum(b for b, _ in white_roses[:k])
    elif  len(orange_roses) > 0 and k>0:
        max_beauty = sum(b for b, _ in orange_roses[:k])
    elif  len(red_roses) > 0 and k>0:
        max_beauty = sum(b for b, _ in red_roses[:k])
    else:
        max_beauty = -1

    return max_beauty


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k, b = int(data[1]), list(map(int, data[2 : 2 + n]))
c = data[2 + n]

# Output the result
print(max_bouquet_beauty(n, k, b, c))