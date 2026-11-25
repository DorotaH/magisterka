import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
p = list(map(int, data[1:]))

operations = 0
for i in range(N):
    if p[i] != i + 1:
        # Find the correct position of p[i]
        correct_pos = p.index(i + 1)
        # Swap p[i] with the element at correct_pos
        p[i], p[correct_pos] = p[correct_pos], p[i]
        # Increment the operation count
        operations += 1

print(operations)
