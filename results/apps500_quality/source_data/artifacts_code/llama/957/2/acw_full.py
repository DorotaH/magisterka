s = input().strip()
heidi = "heidi"
i = 0
for char in s:
	if i < len(heidi) and char == heidi[i]:
		i += 1
if i == len(heidi):
	print("YES")
else:
	print("NO")
