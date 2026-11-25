s = input()

count = sum(bool(s[i] == s[i - 1])
		for i in range(1, len(s)))
print(count)
