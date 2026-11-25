from collections import deque

n, m = map(int, input().split())

boys = deque(range(1, n + 1))
girls = deque(range(1, m + 1))

s = list()
while boys and girls:
    if  boys:
        s.append(f"{boys.popleft()} {girls.pop()}")
    if  boys:
        s.append(f"{boys.pop()} {girls.popleft()}")
    if  not  boys and  not  girls:
        break

print(len(s))
print("\n".join(s))