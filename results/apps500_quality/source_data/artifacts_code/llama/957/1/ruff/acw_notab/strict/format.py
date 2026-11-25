s = input()
target = "heidi"
i = 0
for char in s:
    if i < len(target) and char == target[i]:
        i += 1
if i == len(target):
    print("YES")
else:
    print("NO")
