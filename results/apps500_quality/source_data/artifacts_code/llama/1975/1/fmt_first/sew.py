from  collections import  deque

n, m = map(int, input().split())
boys = deque(range(1, n + 1))
girls = deque(range(1, m + 1))

result = list()
while boys and girls:
    if boys and girls:
        result.append(f"{boys[0]} {girls[0]}")
        boys.popleft()
        girls.popleft()
    else:
        break

print(len(result))
for line in result:
    print(line)