import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
m = int(data[2])
a = int(data[3])

votes = [0] * (1 + n)
last_vote = [0] * (1 + n)

for i in range(a):
    candidate = int(data[i + 4])
    votes[candidate] += 1
    last_vote[candidate] = i

# Sort candidates by votes and then by last vote time
candidates = sorted(range(1, 1 + n), key=lambda x: (-votes[x], last_vote[x]))

# Determine the outcome for each candidate
results = [0] * (1 + n)
for i, candidate in enumerate(candidates):
    if i < k:
        results[candidate] = 1
    elif i < k + m - a:
        results[candidate] = 2
    else:
        results[candidate] = 3

# Print the results for candidates 1 to n
for i in range(1, 1 + n):
    print(results[i], end=" ")
