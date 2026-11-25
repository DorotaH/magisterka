n = int(input())
v = list(map(int, input().split()))
t = list(map(int, input().split()))

stack = []
evaporated = [0] * n

for i in range(n):
	while stack and i >= stack[-1][0]:
		stack.pop()

	evaporated[i] = v[i] - stack[-1][1] if stack else v[i]
	stack.append((i, v[i] - t[i]))

print(*evaporated)
