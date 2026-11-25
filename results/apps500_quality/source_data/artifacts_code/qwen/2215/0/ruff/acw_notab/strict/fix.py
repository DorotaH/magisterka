def maximize_beauty(n, m, visitors):
    # Initialize the array with -1, 0 means rose, 1 means lily
    flowers = [-1] * n

    # Count the number of roses and lilies in each segment
    for l, r in visitors:
        roses = 0
        lilies = 0
        for i in range(l - 1, r):
            if flowers[i] == 0:
                roses += 1
            elif flowers[i] == 1:
                lilies += 1
        if lilies * roses > 0:
            # If both roses and lilies are present, flip the segment to maximize beauty
            for i in range(l - 1, r):
                if flowers[i] == -1:
                    flowers[i] = 0 if lilies < roses else 1
        else:
            # If one type of flower is missing, fill the segment with the missing flower
            if roses == 0:
                for i in range(l - 1, r):
                    if flowers[i] == -1:
                        flowers[i] = 1
            elif lilies == 0:
                for i in range(l - 1, r):
                    if flowers[i] == -1:
                        flowers[i] = 0

    return ''.join('0' if f == 0 else '1' for f in flowers)


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
visitors = [(int(data[2 + i * 2]) - 1, int(data[3 + i * 2])) for i in range(m)]

# Output the result
print(maximize_beauty(n, m, visitors))
