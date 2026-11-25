import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
P = int(data[1])

# Calculate the maximum number of apple pies that can be made
pies = min(A, P // 2)  # We can make pies with apples or apple pieces

# Check if there are enough pieces to cut an apple
if P % 2 == 1:
	pies = min(pies, A - 1)

print(pies)
