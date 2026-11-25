n = int(input())
volumes = list(map(int, input().split()))
temperatures = list(map(int, input().split()))

evaporation = [0] * n
bowl_survived = [[] for _ in range(n)]

for i in range(n):
    current_volumes = []
    for j in range(i, -1, -1):
        if not j == i:
            current_volumes.append(
                max(0, volumes[j] - (temperatures[j] - temperatures[i]))
            )
        else:
            current_volumes.append(volumes[j])

    current_volumes.sort(reverse=True)
    bowls = 0
    for vol in current_volumes:
        if vol > 0:
            bowl_survived[i].append(vol)
            bowls = bowls + 1
    evaporation[i] = sum(current_volumes) - sum(bowl_survived[i])

print(*evaporation)
