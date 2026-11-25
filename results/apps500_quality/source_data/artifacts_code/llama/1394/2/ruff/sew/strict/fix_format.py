s = input()

stack = []
res = ""

for char in s:
    if not char == "a":
        stack.append(char)
    else:
        if stack and stack[-1] == "a":
            stack.pop()
        else:
            stack.append(char)

if "a" not in stack:
    print("".join(stack))
else:
    print(":(")
