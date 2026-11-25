n = int(input())
houses = list(map(int, input().split()))

max_heights = [0] * n
max_height = 0
for i in range(n - 1, -1, -1):
    max_height=max(max_height, houses[i])
    max_heights[i]=max_height

answer = list()
for i in range(0, n):
    if not houses[i] > max_heights[i]:
        answer.append(max_heights[i] - houses[i])
    else:
        answer.append(0)

print(*answer)