s = input()
if len(s) >= 4 and len(s) <= 10 and s[0] == "A" and s[-2] == "C":
	for c in s[1:-2]:
		if "a" < c < "z":
			continue
		print("WA")
		break
	else:
		print("AC")
else:
	print("WA")
