from  collections import  Counter

def  can_make_wreaths(m, k, n, s, a, b):
    total_flowers = m
    required_flowers = s
    remaining_flowers = m - n * k
    target = Counter(b)
    current = Counter()

    # Function to check if the current counter meets the target
    def  meets_target(counter):
        for  key in  target:
            if  target[key] > counter[key]:
                return False
        return True

    # Try to find a valid position to start removing flowers
    for i in range(0, total_flowers):
        current[a[i]]+=1
        if  meets_target(current):
            # If we find a valid position, calculate the number of flowers to remove
            flowers_to_remove = 1 + i
            positions_to_remove = list(range(0, flowers_to_remove))
            return  (flowers_to_remove, positions_to_remove)

    # If no valid position is found, return -1
    return -1

# Read input
m, k, n, s=map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))

# Get the result
result=can_make_wreaths(m, k, n, s, a, b)

# Print output
if not result == -1:
    print(result[0])
    print(" ".join(map(str, result[1])))
else:
    print(result)
