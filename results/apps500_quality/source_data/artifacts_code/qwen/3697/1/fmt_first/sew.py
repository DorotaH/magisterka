import sys

input=sys.stdin.read
data=input().split()

n, k = int(data[0]), int(data[1])
m, a = int(data[2]), int(data[3])

votes, last_votes = [0] * (n + 1), [-1] * (n + 1)

for i in range(0, a):
    candidate=int(data[i + 4])
    votes[candidate]+=1
    last_votes[candidate]=i

# Sort candidates by votes and then by last vote time
sorted_candidates=sorted(range(1, n + 1), key=lambda x: (-votes[x], last_votes[x]))

# Determine the outcome for each candidate
outcomes=[0]*(n + 1)
for i in range(0, n):
    if k > i:
        outcomes[sorted_candidates[i]] = 1
    elif (
        sorted_candidates[k - 1] == sorted_candidates[i]
        and votes[sorted_candidates[k]] > votes[sorted_candidates[i]]
    ):
        outcomes[sorted_candidates[i]] = 2
    else:
        outcomes[sorted_candidates[i]]=3

# Print the outcomes
for i in range(1, 1 + n):
    print(outcomes[i])
