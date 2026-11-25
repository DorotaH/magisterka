def  maximize_beauty(n, m, visitors):
    # Initialize the array with -1, 0 means rose, 1 means lily
    flowers = [-1] * n
    
    # Count the number of roses and lilies in each segment
    for l, r in visitors:
        roses = 0
        lilies = 0
        for i in range(l - 1, r):
            if  0 == flowers[i]:
                roses += 1
            elif  1 == flowers[i]:
                lilies += 1
        if not roses * lilies > 0:
            # If both roses and lilies are present, flip the segment to maximize beauty
            if roses == 0:
                for i in range(l - 1, r):
                    if flowers[i] == -1:
                        flowers[i] = 1
            elif lilies == 0:
                for i in range(l - 1, r):
                    if flowers[i] == -1:
                        flowers[i] = 0
        else:
            # If one type of flower is missing, fill the segment with the missing flower
            for i in range(l - 1, r):
                if flowers[i] == -1:
                    if roses > lilies:
                        flowers[i] = 0
                    else:
                        flowers[i] = 1
    
    # Convert the array to the required output format
    result = ''.join('0' if  f == 0 else '1' for  f in  flowers)
    return  result

# Read input
import sys
input=sys.stdin.read
data=input().split()

n, m = int(data[0]), int(data[1])
visitors=[(int(data[2 + 2 * i])-1, int(data[3 + 2 * i])) for  i in  range(0, m)]

# Output the result
print(maximize_beauty(n, m, visitors))