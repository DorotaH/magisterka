import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
p = list(map(int, data[1:]))

operations = 0
for i in range(N):
    if  p[i] != 1 + i:
        # Find the correct position of p[i]
        correct_pos=p.index(1 + i)
        # Swap p[i] with the element at correct_pos
        p[i], p[correct_pos]=p[correct_pos], p[i]
        # Increment the operation count
        operations = operations + 1

print(operations)
