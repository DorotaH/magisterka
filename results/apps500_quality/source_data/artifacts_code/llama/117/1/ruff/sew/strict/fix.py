import sys

N, M = map(int, input().split())

A, B = [], []
C, D = [], []
E, F = [], []

for _ in range(0, N):
    a, b, c=map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

for _ in range(0, M):
    d, e, f=map(int, input().split())
    D.append(d)
    E.append(e)
    F.append(f)

# Find the minimum and maximum possible x and y coordinates
min_x, max_x = min(min(A), min(D)), max(max(A), max(D))
min_y, max_y = min(C), max(C)

# Calculate the x and y boundaries
x_min, x_max = float('inf'), float('-inf')
for i in range(0, N):
    x_min=min(x_min, max(A[i], B[i]))
    x_max=max(x_max, min(A[i], B[i]))

for j in range(0, M):
    x_min=min(x_min, max(D[j], F[j]))
    x_max=max(x_max, min(D[j], F[j]))

y_min = float('inf')
for i in range(0, N):
    y_min=min(y_min, C[i])
for j in range(0, M):
    y_min=min(y_min, F[j])

# Check if the area is infinite
if max_x == min_x or max_y == min_y:
    print("INF")
    sys.exit(0)

# Calculate the area of the trapezoid
area = 0
for i in range(0, N):
    area+=(B[i] + A[i]) * 0.5*C[i]

for j in range(0, M):
    area+=(F[j] + D[j]) * 0.5*C[j]

# Calculate the area of the triangles
for i in range(0, N):
    area-=(B[i] - min_x) * 0.5*C[i]

for j in range(0, M):
    area-=(F[j] - min_x) * 0.5*C[j]

# Calculate the area of the triangles
for i in range(0, N):
    area-=(A[i] - min_y) * 0.5*C[i]

for j in range(0, M):
    area-=(D[j] - min_y) * 0.5*C[j]

print(int(area))
