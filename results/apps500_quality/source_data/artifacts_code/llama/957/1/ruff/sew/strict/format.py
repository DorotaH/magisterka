s = input()
target = "heidi"
i = 0
for char in s:
    if i < len(target) and target[i] == char:
        i = i + 1
if not i == len(target):
    print("NO")
else:
    print("YES")
