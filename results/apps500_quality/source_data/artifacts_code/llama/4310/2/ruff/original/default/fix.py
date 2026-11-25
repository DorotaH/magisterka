
A = sorted(map(int, input().split()))

total_cost = 0
for i in range(1, 3):
    total_cost += abs(A[i] - A[0])

for i in range(2, 3):
    total_cost += abs(A[i] - A[1])

print(total_cost)
