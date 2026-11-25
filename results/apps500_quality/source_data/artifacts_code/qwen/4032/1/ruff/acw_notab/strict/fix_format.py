def max_problems_solved(n, k, a):
    left = 0
    right = n - 1
    solved = 0

    while left <= right:
        if a[left] <= k:
            solved += 1
            left += 1
        elif a[right] <= k:
            solved += 1
            right -= 1
        else:
            break

    return solved


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
a = list(map(int, data[2:]))

# Output the result
print(max_problems_solved(n, k, a))
