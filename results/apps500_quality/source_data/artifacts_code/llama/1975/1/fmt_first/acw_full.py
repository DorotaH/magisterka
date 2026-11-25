from collections import deque

n, m = map(int, input().split())
boys = deque(range(1, 1 + n))
girls = deque(range(1, 1 + m))

result = []
while boys and girls:
	result.append(f"{boys[0]} {girls[0]}")
	boys.popleft()
	girls.popleft()
print(len(result))
for line in result:
	print(line)
