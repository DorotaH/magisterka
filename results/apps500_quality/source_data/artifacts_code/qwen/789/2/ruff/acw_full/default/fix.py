n = int(input())
index = 0
count = 0

while count < n:
	num = int("".join(sorted(str(i))))
	if str(num).count('4') == str(num).count('7'):
		count += 1
		if count == n:
			index = i
			break
	i += 1

print(index)
