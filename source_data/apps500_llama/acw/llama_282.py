s = input()
count = sum(bool(i == '1')
		for i in s)
print(count)
