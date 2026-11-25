
# Read the number of takoyaki and their deliciousness
N, d = int(input()), list(map(int, input().split()))

# Calculate the sum of the health points restored from eating two takoyaki over all possible choices
total = sum([d[i] * d[j] for i in range(N) for j in range(i + 1, N)], 0)

# Print the result
print(total)