import sys

n = int(input())
balls = sorted(map(int, input().split()))

possible = False

for  i in  range(0, n-2):
    for j in range(1+i, n - 1):
        for k in range(j+1, n):
            if  abs(balls[i] - balls[j]) <= 2 and  abs(balls[j] - balls[k]) <= 2 and  abs(balls[i] - balls[k]) <= 2:
                possible=True
                break
        if possible:
            break
    if possible:
        break

if not possible:
    print("NO")
else:
    print("YES")
