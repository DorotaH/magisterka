import sys

n = int(input())
a = list(map(int, input().split()))

stack = []
dec = False
increasing = True
result = [0] * n

for i in range(n):
	while stack and stack[-1] > a[i]:
		stack.pop()
		dec = True
	if stack and stack[-1] < a[i]:
		increasing = False
	stack.append(a[i])

	result[i] = 0 if increasing else 1
	if stack and stack[-1] == a[i]:
		stack.pop()

if increasing:
	print("YES")
else:
	print("NO")
	sys.exit(0)

increasing = True
stack = []
dec = True
for i in range(n - 1, -1, -1):
	while stack and stack[-1] < a[i]:
		stack.pop()
	if stack and stack[-1] > a[i]:
		increasing = False
	stack.append(a[i])

	if stack and stack[-1] == a[i]:
		stack.pop()

	result[i] = 0 if increasing else 1
if increasing:
	print("YES")
	print(" ".join(map(str, result)))
else:
	print("NO")
