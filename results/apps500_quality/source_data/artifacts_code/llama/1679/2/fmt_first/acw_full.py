n = int(input())
s = input()

decoded = ""
count = 0

for i in range(n):
	if s[i] == "0":
		count += 1
	else:
		decoded += str(count)
		count = 0

print(int(count) + int(decoded))
