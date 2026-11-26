from collections import deque

n, m = map(int, input().split())

boys = deque(range(1, 1 + n))
girls = deque(range(1, 1 + m))

s = []
while boys and girls:
    s.append(f"{boys.popleft()} {girls.pop()}")
    if boys:
        s.append(f"{boys.pop()} {girls.popleft()}")
    if not boys and not girls:
        break

print(len(s))
print("\n".join(s))
