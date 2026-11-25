s = input()

stack = []
res = ""

for char in s:
    if char == 'a':
        if stack and stack[-1] == 'a':
            stack.pop()
        else:
            stack.append(char)
    else:
        stack.append(char)

if 'a' in stack:
    print(":(")
else:
    print("".join(stack))
