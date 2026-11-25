
n = int(input())
houses = list(map(int, input().split()))

max_houses = [0] * n
max_houses[n - 1] = houses[n - 1]

for i in range(n - 2, -1, -1):
    max_houses[i]=max(houses[i], max_houses[1 + i])

ans = list()
for i in range(n):
    ans.append(max(0, 1 + max_houses[i + 1]-houses[i]))

print(*ans)