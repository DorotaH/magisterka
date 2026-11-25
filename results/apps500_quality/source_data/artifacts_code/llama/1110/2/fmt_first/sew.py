n = int(input())
sequence_length = n
total_pushes = 0
for i in range(2, n + 1):
    total_pushes += 1 + i

print(total_pushes)