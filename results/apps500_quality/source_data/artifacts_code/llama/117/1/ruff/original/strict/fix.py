import sys

N, M = map(int, input().split())

A = []
B = []
C = []
D = []
E = []
F = []

for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

for _ in range(M):
    d, e, f = map(int, input().split())
    D.append(d)
    E.append(e)
    F.append(f)

# Find the minimum and maximum possible x and y coordinates
min_x = min(min(A), min(D))
max_x = max(max(A), max(D))
min_y = min(C)
max_y = max(C)

# Calculate the x and y boundaries
x_min = float('inf')
x_max = float('-inf')
for i in range(N):
    x_min = min(x_min, max(A[i], B[i]))
    x_max = max(x_max, min(A[i], B[i]))

for j in range(M):
    x_min = min(x_min, max(D[j], F[j]))
    x_max = max(x_max, min(D[j], F[j]))

y_min = float('inf')
for i in range(N):
    y_min = min(y_min, C[i])
for j in range(M):
    y_min = min(y_min, F[j])

# Check if the area is infinite
if min_x == max_x or min_y == max_y:
    print("INF")
    sys.exit(0)

# Calculate the area of the trapezoid
area = 0
for i in range(N):
    area += 0.5 * (B[i] + A[i]) * C[i]

for j in range(M):
    area += 0.5 * (F[j] + D[j]) * C[j]

# Calculate the area of the triangles
for i in range(N):
    area -= 0.5 * (B[i] - min_x) * C[i]

for j in range(M):
    area -= 0.5 * (F[j] - min_x) * C[j]

# Calculate the area of the triangles
for i in range(N):
    area -= 0.5 * (A[i] - min_y) * C[i]

for j in range(M):
    area -= 0.5 * (D[j] - min_y) * C[j]

print(int(area))
