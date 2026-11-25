n, k = map(int, input().split())

# Initialize a list to store the number of ways for each number of balls
ways = [0] * (n + 1)
ways[0] = 1
ways[1] = k

# For each number of balls from 2 to n
for i in range(2, n + 1):
    # The number of ways to paint i balls is the sum of the number of ways to paint i-1 balls
    # and the number of ways to paint i-2 balls, each multiplied by k
    ways[i] = ((ways[i - 1] * k) + ways[i - 2]) % (2**31 - 1)

print(ways[n])
