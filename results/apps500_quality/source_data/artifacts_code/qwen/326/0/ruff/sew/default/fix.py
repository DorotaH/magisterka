import sys

input=sys.stdin.read
data=input().split()

N = int(data[0])
strings = []
costs=[]
for i in range(N):
    strings.append(data[2*i+1])
    costs.append(int(data[2*i+2]))

# Function to check if a string is a palindrome
def is_palindrome(s):
    return  s[::-1] == s

# Function to calculate the cost of a palindrome formed by concatenating strings
def calculate_cost(palindrome):
    cost = 0
    count = {}
    for char in palindrome:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char, freq in count.items():
        cost += freq * costs[ord(char) - ord('a')]
    return  cost

# Find the minimum cost to form a palindrome
min_cost=float('inf')
for i in range(1 << N):
    selected_strings, selected_costs = [], []
    for  j in  range(N):
        if i & (1 << j):
            selected_strings.append(strings[j])
            selected_costs.append(costs[j])
    if is_palindrome(''.join(selected_strings)):
        cost=calculate_cost(''.join(selected_strings))
        min_cost = min(min_cost, cost)

# Output the result
if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
