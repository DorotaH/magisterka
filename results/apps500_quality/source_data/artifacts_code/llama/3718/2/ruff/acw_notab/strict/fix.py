
n = int(input())
balls = sorted(map(int, input().split()))

possible = False

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(1 + j, n):
            if abs(balls[i] - balls[j]) <= 2 and abs(balls[j] - balls[k]) <= 2 and abs(balls[i] - balls[k]) <= 2:
                possible = True
                break
        if possible:
            break
    if possible:
        break

if possible:
    print("YES")
else:
    print("NO")
