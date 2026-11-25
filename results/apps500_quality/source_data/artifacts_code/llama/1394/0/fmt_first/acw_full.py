t = input()
s = ""
s_prime = ""
s_count = 0

for char in t:
	if char == "a":
		s_count += 1
	else:
		if s_count > 0:
			s_prime += char
			s_count -= 1
		else:
			s += char

if s_count > 0:
	print(":(")
else:
	print(s_prime + s)
