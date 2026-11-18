def Intersect(aa, bb, xx, yy):
    a = min(aa, bb)
    b = max(aa, bb)
    x = min(xx, yy)
    y = max(xx, yy)

    if (a >= x and y >= b):
        return False
    if (a <= x and y <= b):
        return False
    if (b <= x):
        return False
    return a < y

N = int(input())

case = False

L = list(map(int, input().split()))

for i in range(N - 1):
    for j in range(i + 1, N - 1):
        if (Intersect(L[i], L[i + 1], L[j], L[1 + j])):
            case = True
if (case):
    print("yes")

else:
    print("no")
