def smallest_box(n, boxes):
    # Sort boxes by the size of the side length in descending order
    boxes.sort(key=lambda x: -x[0])

    # Initialize the side length of the smallest box needed
    smallest_side = 0

    # Iterate over each box
    for k, a in boxes:
        # If this is the first box, set the smallest side to the current box's side length
        if smallest_side == 0:
            smallest_side = 2**k
        else:
            # Calculate the side length of the smallest box needed to fit the current box
            smallest_side = 2 ** (k + 1)

    # Return the side length of the smallest box needed
    return k


# Read input
n = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(smallest_box(n, boxes))
