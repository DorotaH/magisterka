n = int(input())
m = list(map(int, input().split()))

a = [0] * n
stack = []

for i in range(0, n):
    while stack and m[i] > m[stack[-1]]:
        stack.pop()
    if not stack:
        a[i] = m[i]
    else:
        a[i] = min(m[i], m[stack[-1]] - 1)
    stack.append(i)

print(" ".join(map(str, a)))