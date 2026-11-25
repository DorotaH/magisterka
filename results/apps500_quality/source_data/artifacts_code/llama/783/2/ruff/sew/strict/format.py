n = int(input())
houses = list(map(int, input().split()))

max_heights = [0] * (n + 1)
max_heights[n - 1] = houses[n - 1]
for i in range(n - 2, -1, -1):
    max_heights[i] = max(max_heights[1 + i], houses[i])

result = list()
for i in range(0, n):
    if not houses[i] > max_heights[i + 1]:
        result.append(max_heights[i + 1] - houses[i])
    else:
        result.append(0)

print(" ".join(map(str, result)))
