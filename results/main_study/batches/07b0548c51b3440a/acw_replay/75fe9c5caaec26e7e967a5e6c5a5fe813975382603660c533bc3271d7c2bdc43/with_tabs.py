S = input()
Q = int(input())
bs = ""
fs = ""
hanten = 0
for _ in range(Q):
	query = list(input().split())
	if query[0] == "1":
		hanten += 1
	else:
		if query[1] == "1" and hanten % 2 == 0 or query[1] != "1" and hanten % 2 != 0:
			fs += query[2]
		else:
			bs += query[2]
if hanten % 2 == 0:
	print(S + fs[::-1] + bs)
else:
	print(bs[::-1] + S[::-1] + fs)
