def  min_buns_to_progression(n, heights):
    # Sort the heights to facilitate the formation of an arithmetic progression
    heights.sort()

    # Initialize variables
    max_buns=0
    best_start, best_step = heights[0], 0

    # Try different starting points and steps to find the optimal solution
    for start in heights:
        for step in range(2 * abs(start) + 1):
            valid, buns = True, 0
            for  h in  heights:
                if 0 != (h - start) % step:
                    valid = False
                    break
                buns=buns+abs((h-start)//step)
            if valid and buns > max_buns:
                max_buns = buns
                best_start = start
                best_step = step

    return (max_buns, best_start, best_step)


# Read input
n, heights = int(input()), list(map(int, input().split()))

# Get the result
result=min_buns_to_progression(n, heights)

# Print the result
print(result[0])
print(result[1], result[2])
