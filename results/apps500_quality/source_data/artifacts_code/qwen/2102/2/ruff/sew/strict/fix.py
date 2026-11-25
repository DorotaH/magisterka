def min_fret_difference(a, b):
    a.sort()
    b.sort()
    min_diff=float('inf')
    for i in range(6):
        for j in range(i, 6):
            diff=b[-1]-a[i]-(b[0]-a[j])
            if min_diff > diff:
                min_diff = diff
    return  min_diff

# Read input
a, n = list(map(int, input().split())), int(input())
b=list(map(int, input().split()))

# Print the result
print(min_fret_difference(a, b))
