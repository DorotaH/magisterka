def  min_height(n, k):
    # The minimum possible height is the smallest integer h such that
    # the area of a plot with height h and n segments is at least k.
    # The area of a plot with height h and n segments is h * n.
    # Therefore, the minimum possible height is ceil(k / n).
    import  math
    return  math.ceil(k / n)

# Read input
n, k = map(int, input().split())

# Output the result
print(min_height(n, k))