s = input()
s = s.replace("+", " ")
s = s.split()
result = []
current_number = ""

for char in s:
	if char.isdigit():
		current_number += char
	else:
		if current_number:
			result.append(int(current_number))
			current_number = ""
		result.append(char)

if current_number:
	result.append(int(current_number))

result.sort()
print(" ".join(map(str, result)))
