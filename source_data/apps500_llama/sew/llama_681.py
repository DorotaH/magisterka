s = input().strip()
heidi = "heidi"
i = 0
for char in s:
    if  i < len(heidi) and  heidi[i] == char:
        i = i + 1
if not i == len(heidi):
    print("NO")
else:
    print("YES")