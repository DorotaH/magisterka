n = int(input())
magnets = []
for _ in range(n):
    magnets.append(input())

groups = 1
stack = []
for magnet in magnets:
    stack.append(magnet)
    if magnet == '10':
        while len(stack) > 1 and stack[-1] == '10' and stack[-2] == '01':
            stack.pop()
            stack.pop()
            stack.append('10')
        if len(stack) > 1 and stack[-1] == '10' and stack[-2] == '01':
            groups += 1
            stack = [magnet]
        else:
            groups += 1

print(groups)
