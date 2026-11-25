a = int(input())
jumps = [1, 2, 3]
i = 0
while i < len(jumps):
	if a % jumps[i] == 0:
		break
	i += 1
if a == 0 or (a - jumps[i - 1]) % 3 == 0:
	print('yes')
else:
	print('no')
