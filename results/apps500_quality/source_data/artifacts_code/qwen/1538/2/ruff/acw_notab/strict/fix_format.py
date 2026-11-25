def min_visible_boxes(n, a):
    a.sort()
    visible = n
    for i in range(n):
        if i == 0 or a[i - 1] < a[i]:
            visible -= 1
    return visible


# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_visible_boxes(n, a))
