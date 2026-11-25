import sys
from collections import deque

def can_survive(n, m, w, friends):
    # Initialize a list to keep track of the number of plates left for each food type
    plates_left=[w[i] for i in range(0, n)]
    
    # Initialize a list to store the order in which friends will be called
    order=[]
    
    # Initialize a deque to store the indices of friends whose favorite foods are available
    available_friends=deque()
    
    for i in range(0, m):
        x, y = friends[i]
        if  plates_left[x-1]>0:
            available_friends.append(i)
        if  plates_left[y-1]>0:
            available_friends.append(i)
    
    # Process the available friends
    while  available_friends:
        friend_index=available_friends.popleft()
        x, y=friends[friend_index]
        if  plates_left[x - 1] > 0:
            plates_left[x-1]-=1
        if  plates_left[y - 1] > 0:
            plates_left[y-1]-=1
        order.append(1 + friend_index)
    
    # Check if any plates are left
    if not any(plates_left):
        return "ALIVE", order
    else:
        return "DEAD"

# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
w = list(map(int, data[2:2+n]))
friends = [(int(data[2+n+2*i])-1, int(data[2+n+2*i+1])-1) for i in range(m)]

# Determine if Lee can survive and get the order
result, order = can_survive(n, m, w, friends)

# Output the result
print(result)
if result=="ALIVE":
    print(" ".join(map(str, order)))
