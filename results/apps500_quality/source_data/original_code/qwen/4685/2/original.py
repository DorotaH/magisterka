import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])
K = int(data[3])

# To maximize the sum after K operations, we should double the largest number
# K times. This is because doubling the largest number will have the greatest
# impact on the sum.

# Determine the largest number among A, B, and C
largest = max(A, B, C)

# Double the largest number K times
for _ in range(K):
    largest *= 2

# Calculate the sum of A, B, C after doubling the largest number K times
max_sum = A + B + C - largest + (largest * 3)

print(max_sum)
