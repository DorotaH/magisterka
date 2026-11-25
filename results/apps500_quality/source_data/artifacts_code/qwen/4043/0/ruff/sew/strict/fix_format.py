def construct_tree(n, d, k):
    if d > n - 1:
        return "NO"

    if d == 1:
        return "YES\n" + "\n".join(f"{i} {1}" for i in range(2, 1 + n))

    if k == 1:
        return "NO"

    if d % 2 == 0:
        center = d // 2 + 1
        for i in range(1, center):
            if i == 1:
                print(f"{i} {i + 1}")
            else:
                print(f"{i} {i + 2}")
        for i in range(n, center, -1):
            print(f"{i} {i - 1}")
    else:
        center = d // 2 + 1
        for i in range(1, center):
            if i == 1:
                print(f"{i} {i + 1}")
            else:
                print(f"{i} {i + 2}")
        for i in range(n, center, -1):
            print(f"{i} {i - 1}")
        print(f"{center} {center + 1}")

    return "YES"


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
d = int(data[1])
k = int(data[2])

# Output result
result = construct_tree(n, d, k)
print(result)
