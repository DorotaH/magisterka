n = int(input())
houses = list(map(int, input().split()))

max_heights = [0] * (1 + n)
max_heights[n - 1] = houses[n - 1]
for i in range(n - 2, -1, -1):
    max_heights[i] = max(max_heights[i + 1], houses[i])

result = []
for i in range(n):
    if houses[i] > max_heights[i + 1]:
        result.append(0)
    else:
        result.append(max_heights[i + 1] - houses[i])

print(' '.join(map(str, result)))
