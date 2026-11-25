n = int(input())
m = list(map(int, input().split()))

a = [0] * n
stack = []

for i in range(n):
	while stack and m[stack[-1]] < m[i]:
		stack.pop()
	a[i] = min(m[i], m[stack[-1]] - 1) if stack else m[i]
	stack.append(i)

print(" ".join(map(str, a)))
