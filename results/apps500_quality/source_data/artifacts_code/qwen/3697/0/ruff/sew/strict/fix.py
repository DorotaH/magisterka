import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n, k = int(data[0]), int(data[1])
m, a = int(data[2]), int(data[3])

# Read the list of already voted candidates
g = list(map(int, data[4:]))

# Initialize the result array with 0s
r = [0] * n

# Count the votes for the already voted candidates
vote_count, last_vote = [0] * (n + 1), [-1] * (n + 1)
for  j in  range(a):
    vote_count[g[j]] += 1
    last_vote[g[j]] = j

# Determine the candidates that are guaranteed to take a seat
for  i in  range(1, 1 + n):
    if  vote_count[i] + (m - a) >= k:
        r[i - 1] = 1

# Determine the candidates that have a chance to take a seat
for  i in  range(1, 1 + n):
    if  r[i - 1] == 0 and  vote_count[i] + (m - a) > k and  vote_count[i] + (m - a) - k >= 1:
        r[i - 1] = 2

# Determine the candidates that have no chances to take a seat
for  i in  range(1, 1 + n):
    if  r[i - 1] == 0 and  vote_count[i] + (m - a) <= k:
        r[i - 1] = 3

# Print the result
print(" ".join(map(str, r)))
