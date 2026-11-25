import  sys

n, a = int(input()), list(map(int, input().split()))

stack, dec = [], False
increasing, result = True, [0] * n

for  i in  range(n):
    while stack and stack[-1] > a[i]:
        stack.pop()
        dec = True
    if  stack and  stack[-1] < a[i]:
        increasing = False
    stack.append(a[i])

    if increasing:
        result[i] = 0
    else:
        result[i] = 1

    if  stack:
        if a[i] == stack[-1]:
            stack.pop()

if not increasing:
    print("NO")
    sys.exit(0)
else:
    print("YES")

increasing, stack = True, []
for  i in  reversed(range(n)):
    while stack and a[i] > stack[-1]:
        stack.pop()
        dec = True
    if  stack and  a[i] < stack[-1]:
        increasing = False
    stack.append(a[i])

    if  stack:
        if a[i] == stack[-1]:
            stack.pop()

    if increasing:
        result[i] = 0
    else:
        result[i] = 1

if not increasing:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, result)))