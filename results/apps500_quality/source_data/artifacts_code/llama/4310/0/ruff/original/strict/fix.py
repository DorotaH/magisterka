
A = list(map(int, input().split()))

min_cost = 0
current_position = A[0]

for i in range(1, 3):
    min_cost += abs(A[i] - current_position)
    current_position = A[i]

print(min_cost)
