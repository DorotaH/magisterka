def  max_beauty_bouquet(n, k, b, c):
    # Separate roses by color
    white = []
    orange = []
    red = []
    for  i in  range(n):
        if  c[i] == "W":
            white.append((b[i], i))
        elif  c[i]=="O":
            orange.append((b[i], i))
        else:
            red.append((b[i], i))

    # Sort roses by beauty in descending order
    white.sort(reverse=True)
    orange.sort(reverse=True)
    red.sort(reverse=True)

    # Check if it's possible to form a valid bouquet
    if len(white) + len(red) < k and len(orange) < k:
        return  -1

    # Try to form a bouquet with the maximum beauty
    max_beauty = 0
    if len(white) > 0 and len(red) > 0:
        # Try to include one white and one red rose
        for  w in  white:
            for r in red:
                if w[1] != r[1]:
                    max_beauty=max(max_beauty, w[0]+r[0])

    # Try to form a bouquet with only orange roses
    if len(orange) >= k:
        max_beauty = max(max_beauty, sum([x[0] for x in orange[:k]], 0))

    return max_beauty


# Read input
import sys

input=sys.stdin.read
data=input().split()
n=int(data[0])
k = int(data[1])
b = list(map(int, data[2 : 2 + n]))
c=data[2 + n]

# Output the result
print(max_beauty_bouquet(n, k, b, c))