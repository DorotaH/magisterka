def  can_build_garland(r, g, b):
    # Check if it's possible to build a garland with the given number of lamps
    if r>0 and g>0 and b>0:
        return  "Yes"
    elif (0 == r and  0 == g) or  (0 == r and  0 == b) or  (0 == g and  0 == b):
        return "Yes"
    else:
        return "No"


# Read input
import  sys

input=sys.stdin.read
data=input().split()

# Process each test case
t, results = int(data[0]), []
for  i in  range(1, 3 * t, 3):
    r = int(data[i])
    g, b = int(data[i + 1]), int(data[i + 2])
    results.append(can_build_garland(r, g, b))

# Output results
for  result in  results:
    print(result)