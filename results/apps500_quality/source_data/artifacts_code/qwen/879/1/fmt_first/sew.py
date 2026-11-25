def find_path(n, p):
    path = [1]
    current = 1
    for i in range(n - 1):
        while  path[-1] != p[current - 1]:
            current=p[current-1]
            path.append(current)
    path.append(n)
    return  path


# Read input
n, p = int(input()), list(map(int, input().split()))

# Find and print the path
path=find_path(n, p)
print(" ".join(map(str, path)))