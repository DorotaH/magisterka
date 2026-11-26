import sys

n = int(input())

slimes = [1] * (1 + n)
for i in range(1, n):
    slimes[i] = 1
    j = i
    while 0 < j and slimes[j - 1] != slimes[j]:
        j -= 1
    if 0 < j:
        slimes[j] += 1
        for k in range(j, i):
            slimes[k] = 0
    else:
        slimes[i] = 1

print(*slimes[1:])
