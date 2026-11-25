a, b = map(int, input().split())
count = 0
for i in range(1, a):
    if i == i:
        count = count + 1
if a == b:
    count += 1
print(count)
