a = input()
b = int(input())

digits = sorted(a, reverse=True)
max_num = ""

for d in a:
	while digits and b - int(max_num) >= int(digits[-1]):
		max_num += digits.pop()
		digits.sort(reverse=True)
	b -= int(max_num[-1])

print(max_num)
