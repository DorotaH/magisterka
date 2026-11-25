import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
P = int(data[1])

# Calculate the total number of pieces of apple we can have
total_pieces = A * 3 + P

# Calculate the maximum number of apple pies we can make
max_pies = total_pieces // 2

print(max_pies)
