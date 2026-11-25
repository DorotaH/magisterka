import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])
K = int(data[3])

# To maximize the sum, we should double the largest number each time
max_num = max(A, B, C)
if max_num == A:
    A *= 2
elif max_num == B:
    B *= 2
else:
    C *= 2

# Perform the operation K times
for _ in range(K-1):
    max_num = max(A, B, C)
    if max_num == A:
        A *= 2
    elif max_num == B:
        B *= 2
    else:
        C *= 2

# Output the largest possible sum
print(A + B + C)
