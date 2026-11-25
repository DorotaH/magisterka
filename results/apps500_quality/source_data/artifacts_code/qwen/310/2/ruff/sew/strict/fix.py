def  min_height(n, k):
    # The minimum height is the smallest integer h such that the area under the plot is at least k
    # The area under the plot can be calculated as the sum of the heights of the segments
    # The height of each segment is the difference in the y-coordinates of the two points
    # To minimize the height, we should try to distribute the area as evenly as possible among the segments
    # The number of segments is 2n, so the minimum height is k // (2n)
    # If the area is not perfectly divisible by 2n, we need to round up to the next integer
    # This is because we can only increase the y-coordinate of points with odd x-coordinates by 1
    # Therefore, we need at least one more unit of height to cover the remainder
    return  (k + n - 1) // (2 * n)

# Read input
n, k = map(int, input().split())

# Print output
print(min_height(n, k))
