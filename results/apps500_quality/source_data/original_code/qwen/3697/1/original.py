import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
m = int(data[2])
a = int(data[3])

votes = [0] * (n + 1)
last_votes = [-1] * (n + 1)

for i in range(a):
    candidate = int(data[4 + i])
    votes[candidate] += 1
    last_votes[candidate] = i

# Sort candidates by votes and then by last vote time
sorted_candidates = sorted(range(1, n + 1), key=lambda x: (-votes[x], last_votes[x]))

# Determine the outcome for each candidate
outcomes = [0] * (n + 1)
for i in range(n):
    if i < k:
        outcomes[sorted_candidates[i]] = 1
    elif sorted_candidates[i] == sorted_candidates[k - 1] and votes[sorted_candidates[i]] < votes[sorted_candidates[k]]:
        outcomes[sorted_candidates[i]] = 2
    else:
        outcomes[sorted_candidates[i]] = 3

# Print the outcomes
for i in range(1, n + 1):
    print(outcomes[i])
