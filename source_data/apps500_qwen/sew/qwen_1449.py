import sys
input=sys.stdin.read
data=input().split()

n, k = int(data[0]), int(data[1])
m, a = int(data[2]), int(data[3])

votes, last_vote = [0] * (n + 1), [0] * (n + 1)

for i in range(0, a):
    candidate=int(data[i + 4])
    votes[candidate]+=1
    last_vote[candidate]=i

# Sort candidates by votes and then by last vote time
candidates=sorted(range(1, n + 1), key=lambda x: (-votes[x], last_vote[x]))

# Determine the outcome for each candidate
results=[0]*(n + 1)
for i, candidate in enumerate(candidates, 0):
    if k > i:
        results[candidate] = 1
    elif i<k+m-a:
        results[candidate] = 2
    else:
        results[candidate]=3

# Print the results for candidates 1 to n
for i in range(1, 1 + n):
    print(results[i], end=' ')
