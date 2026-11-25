import sys
input = sys.stdin.read
data = input().split()

N, A = int(data[0]), int(data[1])
B = int(data[2])

min_cost = min(N * A, B)
print(min_cost)