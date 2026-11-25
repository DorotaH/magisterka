N = int(input())
p = list(map(int, input().split()))

diff = 0
for i in range(N):
    if p[i] != i + 1:
        diff += 1

# Check if the differences are consecutive integers
if diff == 1:
    i = 0
    for j in range(1, diff):
        if abs(p[i] - (p[i] - 1)) != 1:
            diff += 1
            break
        i += 1

print(diff)
