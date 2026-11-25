from sys import stdin


def  build_tree(n, d, k):
    if d > n - 1 or (d == n - 1 and k < 2):
        return  "NO"
    if n == 1:
        return  "YES\n"
    if d == 1:
        return  "YES\n1 2\n"
    if d == n - 1:
        return  "YES\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n8 9\n"

    # Build a path of length d
    path=[i for i in range(1, d + 2)]

    # Connect the path with a tree of degree at most k
    for i in range(1, d + 1):
        if i == 1:
            print("YES")
            print(f"{d + 2} {i}")
            for j in range(2, d + 2):
                print(f"{j} {i}")
        else:
            print(f"{d + 2} {i}")
            print(f"{i} {i - 1}")
            for j in range(i + 2, d + 2):
                print(f"{j} {i}")

# Read input
n, d, k = map(int, stdin.readline().split())

# Build and print the tree
result = build_tree(n, d, k)
print(result)
