s = input()
count = sum(bool(c == "1")
		for c in s)
print(count)
