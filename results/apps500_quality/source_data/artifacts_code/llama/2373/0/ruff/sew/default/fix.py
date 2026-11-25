N = int(input())
p = list(map(int, input().split()))

diff = 0
for i in range(N):
    if  p[i]!=1 + i:
        diff += 1

# Check if the differences are consecutive integers
if diff == 1:
    i = 0
    for  j in  range(1, diff):
        if  1 != abs(p[i] - (p[i] - 1)):
            diff += 1
            break
        i = i + 1

print(diff)