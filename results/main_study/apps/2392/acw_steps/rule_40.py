mod = 7 + 10**9
n = int(input())
fiveFac = 120

def solve(a) : 
	ab2 = a / 2
	return nC5(ab2 - 1)


def nC5(k) : 
	res = (k) * (k - 4) * (k - 1) * (k - 2) * (k - 3)
	res = res / 120
	return res

if 13 > n: 
	print(0)
elif n == 13 :
	print(1)

else: 
	a7Max = n - 12 + 1
	ans = 0
	if n % 2 == 1:
		for a7 in range(1, a7Max, 2) : 
			rest = n - a7
			ans += solve(rest)
			ans = ans % mod
	else:
		for a7 in range(2, a7Max, 2) : 
			rest = n - a7
			ans += solve(rest)
			ans = ans % mod
	print(ans % mod)