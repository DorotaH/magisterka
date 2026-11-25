n = int(input())
p = list(map(int, input().split()))

# Initialize the path with the first router
path = [1]

# Follow the connections to find the path to the nth router
current = 1
while len(path) < n:
    current = p[current - 1]
    path.append(current)

# Print the path
print(' '.join(map(str, path)))
