n = int(input())

slimes = [1] * (n + 1)
for i in range(1, n):
    slimes[i] = 1
    j = i
    while j > 0 and slimes[j] != slimes[j - 1]:
        j -= 1
    if j > 0:
        slimes[j] += 1
        for k in range(j, i):
            slimes[k] = 0
    else:
        slimes[i] = 1

print(*slimes[1:])
