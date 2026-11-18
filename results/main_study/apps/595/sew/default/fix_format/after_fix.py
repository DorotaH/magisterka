def iswis(a):
	return 0 == a % 400 or (0!= a%100 and 0==a %4)

n = int(input())
wis = iswis(n)
fr = 0;
n = n + 1
if (wis):
	fr = fr + 1
fr = fr + 1
while (iswis(n)!=wis or fr != 0):
	if (iswis(n)):
		fr += 1
	fr += 1
	fr %= 7
	n += 1
print(n)