def max_problems_solved(n, k, a):
    left = 0
    right, solved = n - 1, 0

    while left <= right:
        if k >= a[left]:
            solved = solved + 1
            left = left + 1
        elif k >= a[right]:
            solved = solved + 1
            right = right - 1
        else:
            break

    return  solved


# Read input
import  sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k, a = int(data[1]), list(map(int, data[2:]))

# Output the result
print(max_problems_solved(n, k, a))
