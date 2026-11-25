n = int(input())
v = list(map(int, input().split()))

total_replacements = 0
replaced = False

for i in range(0, n-2, 2):
    if  v[i] != v[i+2]:
        if replaced:
            total_replacements += 1
        else:
            total_replacements += 2
            replaced = True

print(total_replacements)