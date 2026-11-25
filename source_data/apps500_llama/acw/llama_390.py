n = int(input())
sequence_length = n
total_pushes = sum(i + 1 for i in range(2, 1 + n))
print(total_pushes)
